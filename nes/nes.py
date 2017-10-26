import yaml
from .bus import Bus
from .clock import ClockGenerator
from .cpu import Cpu
from .memory import AddressRange, MemoryMap, Ram
from .memory.memory_control_unit import MemoryControlUnit


class Nes:
    def __init__(self, yaml_data):
        self.clock = ClockGenerator(yaml_data['clock'])
        self.cartridge = None

        self.buses = {}
        for bus_data in yaml_data['buses']:
            bus = Bus(**bus_data)
            self.buses[bus.name] = bus

        self.cpu = Cpu.create(yaml_data['cpu']['filename'], self)
        self.cpu_mem = MemoryControlUnit(self)

        self.clock.subscribe('cycle-start', self.cpu)
        self.clock.subscribe('ab-ready', self.cpu_mem)
        self.clock.subscribe('db-ready', self.cpu)

        ppu_mem = MemoryMap(0x4000)
        ppu_mem.add_memory(AddressRange(0x0000, 0x1000), Ram(0x1000))  # Pattern Table 0
        ppu_mem.add_memory(AddressRange(0x1000, 0x1000), Ram(0x1000))  # Pattern Table 1
        ppu_mem.add_memory(AddressRange(0x2000, 0x0400), Ram(0x0400))  # Name Table 0
        ppu_mem.add_memory(AddressRange(0x2400, 0x0400), Ram(0x0400))  # Name Table 1
        ppu_mem.add_memory(AddressRange(0x2800, 0x0400), Ram(0x0400))  # Name Table 2
        ppu_mem.add_memory(AddressRange(0x2C00, 0x0400), Ram(0x0400))  # Name Table 3
        ppu_mem.add_memory(AddressRange(0x3F00, 0x0020), Ram(0x0020))  # Palette RAM indexes

        oam_mem = MemoryMap(256)
        oam_mem.add_memory(AddressRange(0x00, 256), Ram(256))

    @staticmethod
    def create(filename):
        with open(filename, 'rt') as stream:
            yaml_data = yaml.load(stream)
            return Nes(yaml_data)

    def insert_cartridge(self, cartridge):
        self.cartridge = cartridge
        self.cpu_mem.memory.add_memory(AddressRange(0x6000, 0xA000), cartridge.mmc)

    def remove_cartridge(self):
        self.cpu.memory.remove_memory(self.cartridge.mmc)
        self.cartridge = None

    def power_up(self):
        self.cpu.power_on()
        self.clock.run()
