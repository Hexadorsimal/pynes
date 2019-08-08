from .cpu import Cpu
from .ppu import Ppu
from .bus import Bus
from .memory import AddressRange, Ram
from .ppu.ppu_register_set import PpuRegisterSet


class Nes:
    def __init__(self, config):
        self.cpu_bus = Bus('cpu')
        self.ppu_bus = Bus('ppu')

        self.ppu = Ppu(self.ppu_bus, config['ppu'])
        self.cpu = Cpu(self.cpu_bus)
        self.cartridge = None

    def insert_cartridge(self, cartridge):
        self.cartridge = cartridge
        self.cpu_bus.add_device(cartridge)
        self.ppu_bus.add_device(cartridge)

    def remove_cartridge(self):
        self.ppu_bus.remove_device(self.cartridge)
        self.cpu_bus.remove_device(self.cartridge)
        self.cartridge = None

    def power_up(self):
        self.cpu.power_on()
