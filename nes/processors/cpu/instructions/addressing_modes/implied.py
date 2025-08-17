from typing import Never

from .addressing_mode import AddressingMode
from ... import Cpu


class ImpliedAddressingMode(AddressingMode):
    @property
    def instruction_size(self):
        return 1

    def calculate_address(self, cpu: Cpu, parameter: int) -> Never:
        raise RuntimeError('This should never be called')

    def read_source(self, processor, parameter):
        raise RuntimeError('This should never be called')

    def write_result(self, processor, parameter, value):
        raise RuntimeError('This should never be called')
