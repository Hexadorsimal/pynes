from nes.cpu.cycle import Cycle
from nes.cpu.microinstructions import Compare
from ..addressing_modes import *
from .instruction import Instruction


class Cpx(Instruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([Compare('X', 'DL')]))
        self.addressing_modes = {
            0xE0: ImmediateAddressing,
            0xE4: ZeroPageAddressing,
            0xEC: AbsoluteAddressing,
        }

    @property
    def name(self):
        return 'CPX'

    @property
    def description(self):
        return 'Compare Memory and Index X'
