from nes.cpu.cycle import Cycle
from nes.cpu.microinstructions import Decrement
from ..addressing_modes import *
from .instruction import Instruction


class Dec(Instruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([Decrement('DL')]))
        self.addressing_modes = {
            0xC6: ZeroPageAddressing,
            0xD6: ZeroPageXAddressing,
            0xCE: AbsoluteAddressing,
            0xDE: AbsoluteXAddressing,
        }

    @property
    def name(self):
        return 'DEC'

    @property
    def description(self):
        return 'Decrement Memory by One'
