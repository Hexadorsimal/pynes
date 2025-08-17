from nes.processors.cpu import Cpu
from .addressing_mode import AddressingMode


class AbsoluteAddressingMode(AddressingMode):
    @property
    def instruction_size(self) -> int:
        return 3

    def calculate_address(self, cpu: Cpu, parameter: int) -> int:
        return parameter
