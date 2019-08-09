from .cpu import Cpu
from .ppu import Ppu
from .bus import Bus


class Nes:
    def __init__(self, config):
        self.cartridge = None
        self.ppu = Ppu(Bus('ppu'), config['ppu'])
        self.cpu = Cpu(Bus('cpu'))

    def insert_cartridge(self, cartridge):
        self.cartridge = cartridge
        self.cpu.bus.add_device(cartridge)
        self.ppu.bus.add_device(cartridge)

    def remove_cartridge(self):
        self.ppu.bus.remove_device(self.cartridge)
        self.cpu.bus.remove_device(self.cartridge)
        self.cartridge = None

    def power_up(self):
        self.cpu.power_on()
