from nes.cpu.cycle import Cycle
from nes.cpu.microinstructions import RotateRight
from ..addressing_modes import *
from .instruction import Instruction


class Ror(Instruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([RotateRight('DL', 'DL')]))
        self.addressing_modes = {
            0x6A: AccumulatorAddressing,
            0x66: ZeroPageAddressing,
            0x76: ZeroPageXAddressing,
            0x6E: AbsoluteAddressing,
            0x7E: AbsoluteXAddressing,
        }

    @property
    def name(self):
        return 'ROR'

    @property
    def description(self):
        return 'Rotate One Bit Right (Memory or Accumulator)'
