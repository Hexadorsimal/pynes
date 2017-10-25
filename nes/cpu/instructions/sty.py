from nes.cpu.cycle import Cycle
from nes.cpu.microinstructions import Move
from ..addressing_modes import *
from .instruction import Instruction


class Sty(Instruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([Move('Y', 'DL')]))
        self.addressing_modes = {
            0x84: ZeroPageAddressing,
            0x94: ZeroPageXAddressing,
            0x8C: AbsoluteAddressing,
        }

    @property
    def name(self):
        return 'STY'

    @property
    def description(self):
        return 'Store Index Y in Memory'
