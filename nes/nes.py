import pygame

from .processors.cpu import Cpu
from .processors.ppu import Ppu, PaletteRam
from .bus import Bus
from .bus.devices.memory import Ram
from .bus.devices import ApuIoRegisterSet

from .processors.instructions import factory


class Nes:
    def __init__(self, config: dict):
        self.master_clock = 0
        self.cartridge = None

        self.cpu_bus = Bus()
        self.ppu_bus = Bus()

        self.cpu = Cpu(self.cpu_bus, factory)
        self.ppu = Ppu(self.ppu_bus, self.cpu, config['ppu'])

        if config['television_standard'] == 'ntsc':
            self.clock_dividers = {'cpu': 12, 'ppu': 4, 'apu': 1}
        elif config['television_standard'] == 'pal':
            self.clock_dividers = {'cpu': 16, 'ppu': 5, 'apu': 1}

        self.ppu_bus.attach_device('Nametable Ram', Ram(0x1000), addr=0x2000, size=0x1F00)
        self.ppu_bus.attach_device('Palette Ram', PaletteRam(), addr=0x3F00, size=0x100)

        self.cpu_bus.attach_device('RAM', Ram(0x0800), addr=0x0000, size=0x2000)
        self.cpu_bus.attach_device('PPU Registers', self.ppu.register_set, addr=0x2000, size=0x2000)
        self.cpu_bus.attach_device('APU/IO Registers', ApuIoRegisterSet(self.ppu), addr=0x4000, size=0x0020)

        self.screen = None

    def insert_cartridge(self, cartridge):
        self.cartridge = cartridge
        self.cpu_bus.attach_device('Cart Bus (CPU)', cartridge.buses['cpu'], addr=0x6000, size=0xA000)
        self.ppu_bus.attach_device('Cart Bus (PPU)', cartridge.buses['ppu'], addr=0x0000, size=0x2000)

    def remove_cartridge(self):
        self.ppu_bus.detach_device(self.cartridge.buses['ppu'])
        self.cpu_bus.detach_device(self.cartridge.buses['cpu'])

        self.cartridge = None

    def startup(self):
        self.cpu.power_on()
        self.ppu.power_on()

    def main_loop(self):
        done = False

        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True

            for processor_name, processor in [('cpu', self.cpu), ('ppu', self.ppu)]:
                divider = self.clock_dividers[processor_name]
                if self.master_clock % divider == 0:
                    processor.tick()

            self.master_clock += 1

    def shutdown(self):
        self.ppu.power_off()
        self.cpu.power_off()
