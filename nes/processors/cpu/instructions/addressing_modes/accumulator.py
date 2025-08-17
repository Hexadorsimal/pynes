from typing import Never

from .addressing_mode import AddressingMode
from ... import Cpu


class AccumulatorAddressingMode(AddressingMode):
    @property
    def instruction_size(self) -> int:
        return 1

    def calculate_address(self, cpu: Cpu, parameter: int) -> Never:
        raise RuntimeError('This should never be called')

    def read_source(self, cpu: Cpu, parameter: int) -> int:
        return cpu.a.value

    def write_result(self, cpu: Cpu, parameter: int, value: int) -> None:
        cpu.a.value = value
