from nes.cpu.cycle import Cycle
from nes.cpu.microinstructions import RotateLeft
from ..addressing_modes import *
from .instruction import Instruction


class Rol(Instruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([RotateLeft('DL', 'DL')]))
        self.addressing_modes = {
            0x2A: AccumulatorAddressing,
            0x26: ZeroPageAddressing,
            0x36: ZeroPageXAddressing,
            0x2E: AbsoluteAddressing,
            0x3E: AbsoluteXAddressing,
        }

    @property
    def name(self):
        return 'ROL'

    @property
    def description(self):
        return 'Rotate One Bit Left (Memory or Accumulator)'
