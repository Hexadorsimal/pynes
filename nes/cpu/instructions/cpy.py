from nes.cpu.cycle import Cycle
from nes.cpu.microinstructions import Compare
from ..addressing_modes import *
from .instruction import Instruction


class Cpy(Instruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([Compare('Y', 'DL')]))
        self.addressing_modes = {
            0xC0: ImmediateAddressing,
            0xC4: ZeroPageAddressing,
            0xCC: AbsoluteAddressing,
        }

    @property
    def name(self):
        return 'CPY'

    @property
    def description(self):
        return 'Compare Memory and Index Y'
