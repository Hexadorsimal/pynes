from .addressing_mode import AddressingMode
from nes.processors.cpu import Cpu


class IndirectAddressingMode(AddressingMode):
    @property
    def instruction_size(self) -> int:
        return 3

    def calculate_address(self, cpu: Cpu, parameter: int) -> int:
        lo_addr = parameter
        hi_addr = (lo_addr + 1) & 0xffff
        lo = cpu.read(lo_addr)
        hi = cpu.read(hi_addr)
        return (hi << 8) | lo
