from typing import Never

from .addressing_mode import AddressingMode
from ... import Cpu


class RelativeAddressingMode(AddressingMode):
    @property
    def instruction_size(self) -> int:
        return 2

    def calculate_address(self, cpu: Cpu, parameter: int) -> int:
        return cpu.pc.value + parameter

    def read_source(self, cpu: Cpu, parameter: int) -> int:
        return self.calculate_address(cpu, parameter)

    def write_result(self, cpu: Cpu, parameter: int, value: int) -> Never:
        raise RuntimeError('This should never be called')
