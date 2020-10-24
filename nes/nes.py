from .processors.cpu import Cpu, PpuRegisterSet, ApuIoRegisterSet
from .processors.ppu import Ppu, PaletteRam
from .processors.apu import Apu
from .bus import Bus
from .memory import Ram


class Nes:
    def __init__(self, config):
        self.master_clock = 0
        self.cartridge = None
        self.buses = {
            'cpu': Bus('cpu'),
            'ppu': Bus('ppu'),
        }

        self.processors = {
            'ppu': Ppu(self.buses['ppu'], config['ppu']),
            'cpu': Cpu(self.buses['cpu']),
            'apu': Apu(None),
        }

        if config['television_standard'] == 'ntsc':
            self.clock_dividers = {'cpu': 12, 'ppu': 4, 'apu': 1}
        elif config['television_standard'] == 'pal':
            self.clock_dividers = {'cpu': 16, 'ppu': 5, 'apu': 1}

        self.buses['ppu'].attach_device(PaletteRam(), addr=0x3F00, size=0x100)

        self.buses['cpu'].attach_device(Ram(0x0800), addr=0x0000, size=0x2000)
        self.buses['cpu'].attach_device(PpuRegisterSet(self.processors['ppu']), addr=0x2000, size=0x2000)
        self.buses['cpu'].attach_device(ApuIoRegisterSet(), addr=0x4000, size=0x0020)

    def insert_cartridge(self, cartridge):
        self.cartridge = cartridge
        cartridge.connect(self.buses)

    def remove_cartridge(self):
        self.cartridge.disconnect(self.buses)
        self.cartridge = None

    def power_up(self):
        for processor in self.processors.values():
            processor.power_on()

        while True:
            for processor_name, processor in self.processors.items():
                divider = self.clock_dividers[processor_name]
                if self.master_clock % divider == 0:
                    processor.tick()

            self.master_clock += 1
