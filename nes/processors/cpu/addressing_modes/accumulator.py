from typing import Never

from .addressing_mode import AddressingMode
from nes.processors.cpu import Cpu


class AccumulatorAddressingMode(AddressingMode):
    @property
    def instruction_size(self) -> int:
        return 1
