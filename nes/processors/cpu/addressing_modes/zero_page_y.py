from .addressing_mode import AddressingMode
from nes.processors.cpu import Cpu


class ZeroPageYAddressingMode(AddressingMode):
    @property
    def instruction_size(self) -> int:
        return 2

    def calculate_address(self, cpu: Cpu, parameter: int) -> int:
        return (parameter + cpu.y.value) & 0x00ff
