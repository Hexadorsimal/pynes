from .cpu import Cpu
from .ppu import Ppu
from .memory import AddressRange, MemoryMap, Ram
from .ppu.ppu_register_set import PpuRegisterSet


class Nes:
    def __init__(self):
        self.cartridge = None

        self.ppu = Ppu()

        self.cpu_mem = MemoryMap(0x10000)
        self.cpu_mem.add_memory(AddressRange(0x0000, 0x2000), Ram(0x0800))  # RAM
        self.cpu_mem.add_memory(AddressRange(0x2000, 0x2000), PpuRegisterSet(self.ppu))  # PPU Registers
        self.cpu_mem.add_memory(AddressRange(0x4000, 0x0018), Ram(0x0018))  # APU and IO Registers
        self.cpu_mem.add_memory(AddressRange(0x4018, 0x0008), Ram(0x0008))  # Disabled APU and IO functionality

        self.cpu = Cpu(self.cpu_mem)

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

    def insert_cartridge(self, cartridge):
        self.cartridge = cartridge
        self.cpu_mem.add_memory(AddressRange(0x6000, 0xA000), cartridge.mmc)

    def remove_cartridge(self):
        self.cpu_mem.remove_memory(self.cartridge.mmc)
        self.cartridge = None

    def power_up(self):
        self.cpu.power_on()
