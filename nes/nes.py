from .processors.cpu import Cpu, PpuRegisterSet
from .processors.ppu import Ppu, NameTableRam, PaletteRam
from .bus import Bus


class Nes:
    def __init__(self, config):
        self.cartridge = None
        self.ppu = Ppu(Bus('ppu'), config['ppu'])
        self.ppu.bus.attach_device(PaletteRam(), 0x3F00, 0xFF)
        # self.ppu.bus.attach_device(NameTableRam())

        self.cpu = Cpu(Bus('cpu'))
        self.cpu.bus.attach_device(PpuRegisterSet(self.ppu), 0x0000, 8)

    def insert_cartridge(self, cartridge):
        self.cartridge = cartridge
        self.cpu.bus.attach_device(cartridge.cpu_device, 0x0000, 256)
        self.ppu.bus.attach_device(cartridge.ppu_device, 0x0000, 256)

    def remove_cartridge(self):
        self.ppu.bus.remove_device(self.cartridge.ppu_device)
        self.cpu.bus.remove_device(self.cartridge.cpu_device)
        self.cartridge = None

    def power_up(self):
        self.ppu.power_on()
        self.cpu.power_on()

        while True:
            self.ppu.step()
            # self.cpu.step()
