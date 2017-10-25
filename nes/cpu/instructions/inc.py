from nes.cpu.cycle import Cycle
from nes.cpu.microinstructions import Increment
from ..addressing_modes import *
from .instruction import Instruction


class Inc(Instruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([Increment('DL')]))
        self.addressing_modes = {
            0xE6: ZeroPageAddressing,
            0xF6: ZeroPageXAddressing,
            0xEE: AbsoluteAddressing,
            0xFE: AbsoluteXAddressing,
        }

    @property
    def name(self):
        return 'INC'

    @property
    def description(self):
        return 'Increment Memory by One'
