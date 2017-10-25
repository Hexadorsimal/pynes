from nes.cpu.cycle import Cycle
from nes.cpu.microinstructions import LogicalShiftRight
from ..addressing_modes import *
from .instruction import Instruction


class Lsr(Instruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([LogicalShiftRight('A', 'A')]))
        self.addressing_modes = {
            0x4A: AccumulatorAddressing,
            0x46: ZeroPageAddressing,
            0x56: ZeroPageXAddressing,
            0x4E: AbsoluteAddressing,
            0x5E: AbsoluteXAddressing,

        }

    @property
    def name(self):
        return 'LSR'

    @property
    def description(self):
        return 'Shift One Bit Right (Memory or Accumulator)'
