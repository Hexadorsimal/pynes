from system.cpu import Processor
from system.memory import AddressRange, MemoryMap, Ram


def run(filename):
    cpu = Processor.load(filename)
    memmap = MemoryMap()
    memmap.add_memory(AddressRange(0x0000, 0x2000), Ram(0x0800))  # RAM
    memmap.add_memory(AddressRange(0x2000, 0x2000), Ram(0x0008))  # PPU Registers
    memmap.add_memory(AddressRange(0x4000, 0x0020), Ram(0x0020))  # APU and IO Registers
    memmap.add_memory(AddressRange(0x4020, 0xBFE0), Ram(0x0008))  # PPU Registers

    memmap.add_memory(AddressRange(0xFFFA, 0x0002), Ram(0x0002))  # NMI vector
    memmap.add_memory(AddressRange(0xFFFC, 0x0002), Ram(0x0002))  # Reset vector
    memmap.add_memory(AddressRange(0xFFFE, 0x0002), Ram(0x0002))  # IRQ/BRK vector

    cpu.step()


if __name__ == '__main__':
    run('system/cpu/6502.yaml')
