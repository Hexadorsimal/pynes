import pygame

from .processors.cpu import Cpu
from .processors.ppu import Ppu, PaletteRam
from .bus import Bus
from .bus.devices.memory import Ram
from .bus.devices import ApuIoRegisterSet


class Nes:
    def __init__(self, config):
        self.master_clock = 0
        self.cartridge = None
        self.buses = {
            'cpu': Bus(),
            'ppu': Bus(),
        }

        cpu = Cpu(self.buses['cpu'])
        ppu = Ppu(self.buses['ppu'], cpu, config['ppu'])

        self.processors = {
            'ppu': ppu,
            # 'cpu': cpu,
        }

        if config['television_standard'] == 'ntsc':
            self.clock_dividers = {'cpu': 12, 'ppu': 4, 'apu': 1}
        elif config['television_standard'] == 'pal':
            self.clock_dividers = {'cpu': 16, 'ppu': 5, 'apu': 1}

        self.buses['ppu'].attach_device('Nametable Ram', Ram(0x1000), addr=0x2000, size=0x1F00)
        self.buses['ppu'].attach_device('Palette Ram', PaletteRam(), addr=0x3F00, size=0x100)

        self.buses['cpu'].attach_device('RAM', Ram(0x0800), addr=0x0000, size=0x2000)
        self.buses['cpu'].attach_device('PPU Registers', self.processors['ppu'].register_set, addr=0x2000, size=0x2000)
        self.buses['cpu'].attach_device('APU/IO Registers', ApuIoRegisterSet(ppu), addr=0x4000, size=0x0020)

        self.screen = None

    @property
    def ppu(self):
        return self.processors['ppu']

    @property
    def cpu(self):
        return self.processors['cpu']

    def insert_cartridge(self, cartridge):
        self.cartridge = cartridge
        self.buses['cpu'].attach_device('Cart Bus (CPU)', cartridge.buses['cpu'], addr=0x6000, size=0xA000)
        self.buses['ppu'].attach_device('Cart Bus (PPU)', cartridge.buses['ppu'], addr=0x0000, size=0x2000)

    def remove_cartridge(self):
        for bus in ['cpu', 'ppu']:
            self.buses[bus].detach_device(self.cartridge.buses[bus])

        self.cartridge = None

    def startup(self):
        for processor in self.processors.values():
            processor.power_on()

    def main_loop(self):
        done = False

        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True

            for processor_name, processor in self.processors.items():
                divider = self.clock_dividers[processor_name]
                if self.master_clock % divider == 0:
                    processor.tick()

            self.master_clock += 1

    def shutdown(self):
        for processor in self.processors.values():
            processor.power_off()
