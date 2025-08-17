from .addressing_mode import AddressingMode
from ... import Cpu


class IndirectIndexedAddressingMode(AddressingMode):
    @property
    def instruction_size(self) -> int:
        return 2

    def calculate_address(self, cpu: Cpu, parameter: int) -> int:
        lo_addr = parameter
        hi_addr = (lo_addr + 1) & 0x00ff
        lo = cpu.read(lo_addr)
        hi = cpu.read(hi_addr)
        addr = (hi << 8) | lo
        return (addr + cpu.y.value) & 0xffff
