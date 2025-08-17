from .addressing_mode import AddressingMode
from ... import Cpu


class IndexedIndirectAddressingMode(AddressingMode):
    @property
    def instruction_size(self) -> int:
        return 2

    def calculate_address(self, cpu: Cpu, parameter: int) -> int:
        lo_addr = (parameter + cpu.x.value) & 0x00ff
        hi_addr = (lo_addr + 1) & 0x00ff
        lo = cpu.read(lo_addr)
        hi = cpu.read(hi_addr)
        return (hi << 8) | lo
