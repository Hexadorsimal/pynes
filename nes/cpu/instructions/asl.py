from nes.cpu.cycle import Cycle
from nes.cpu.microinstructions import ArithmeticShiftLeft
from ..addressing_modes import *
from .instruction import Instruction


class Asl(Instruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([ArithmeticShiftLeft('DL', 'DL')]))

        self.addressing_modes = {
            0x0A: AccumulatorAddressing,
            0x06: ZeroPageAddressing,
            0x16: ZeroPageXAddressing,
            0x0E: AbsoluteAddressing,
            0x1E: AbsoluteXAddressing,
        }

    @property
    def name(self):
        return 'ASL'

    @property
    def description(self):
        return 'Shift left One Bit (Memory or Accumulator)'
