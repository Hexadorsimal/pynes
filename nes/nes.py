from .cpu import Cpu
from .ppu import Ppu
from .bus import Bus
from .memory import AddressRange, Ram
from .ppu.ppu_register_set import PpuRegisterSet


class Nes:
    def __init__(self, config):
        self.bus = Bus()
        self.ppu = Ppu(self.bus, config['ppu'])
        self.cpu = Cpu(self.bus)
        self.cartridge = None

    def insert_cartridge(self, cartridge):
        self.cartridge = cartridge
        self.bus.add_device(cartridge)

    def remove_cartridge(self):
        self.bus.remove_device(self.cartridge)
        self.cartridge = None

    def power_up(self):
        self.cpu.power_on()
