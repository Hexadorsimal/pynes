from typing import Never

from .addressing_mode import AddressingMode
from ... import Cpu


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

    def read_source(self, cpu: Cpu, parameter: int) -> Never:
        raise RuntimeError('This should never be called')

    def write_result(self, cpu: Cpu, parameter: int, value: int) -> Never:
        raise RuntimeError('This should never be called')
