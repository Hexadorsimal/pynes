from .cartridge import RomFile
from .cpu import Processor
from .memory import AddressRange, MemoryMap, Ram


class Nes:
    def __init__(self, cpu):
        self.cartridge = None
        self.cpu = cpu

        self.cpu_mem = MemoryMap()
        self.cpu_mem.add_memory(AddressRange(0x0000, 0x2000), Ram(0x0800))  # RAM
        self.cpu_mem.add_memory(AddressRange(0x2000, 0x2000), Ram(0x0008))  # PPU Registers
        self.cpu_mem.add_memory(AddressRange(0x4000, 0x0018), Ram(0x0018))  # APU and IO Registers
        self.cpu_mem.add_memory(AddressRange(0x4018, 0x0008), Ram(0x0008))  # Disabled APU and IO functionality
        self.cpu_mem.add_memory(AddressRange(0x4020, 0xBFE0), Ram(0xBFE0))  # Cartridge space

        ppu_mem = MemoryMap()
        ppu_mem.add_memory(AddressRange(0x0000, 0x1000), Ram(0x1000))  # Pattern Table 0
        ppu_mem.add_memory(AddressRange(0x1000, 0x1000), Ram(0x1000))  # Pattern Table 1
        ppu_mem.add_memory(AddressRange(0x2000, 0x0400), Ram(0x0400))  # Name Table 0
        ppu_mem.add_memory(AddressRange(0x2400, 0x0400), Ram(0x0400))  # Name Table 1
        ppu_mem.add_memory(AddressRange(0x2800, 0x0400), Ram(0x0400))  # Name Table 2
        ppu_mem.add_memory(AddressRange(0x2C00, 0x0400), Ram(0x0400))  # Name Table 3
        ppu_mem.add_memory(AddressRange(0x3F00, 0x0020), Ram(0x0020))  # Palette RAM indexes

        oam_mem = MemoryMap()
        oam_mem.add_memory(AddressRange(0x00, 256), Ram(256))

    @staticmethod
    def create(filename):
        cpu = Processor.load(filename)
        return Nes(cpu)

    def load_cartridge(self, filename):
        self.cartridge = RomFile.load(filename)

    def power_up(self):
        self.cpu.reset()

        while True:
            self.cpu.step()
