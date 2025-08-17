from .addressing_mode import AddressingMode
from ... import Cpu


class ZeroPageAddressingMode(AddressingMode):
    @property
    def instruction_size(self) -> int:
        return 2

    def calculate_address(self, cpu: Cpu, parameter: int) -> int:
        return parameter
