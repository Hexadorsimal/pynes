from nes.cpu.cycle import Cycle
from nes.cpu.microinstructions import Branch
from ..addressing_modes import RelativeAddressing
from .instruction import Instruction


class Bpl(Instruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([Branch('N', False)]))
        self.addressing_modes = {
            0x10: RelativeAddressing
        }

    @property
    def name(self):
        return 'BPL'

    @property
    def description(self):
        return 'Branch on Result Plus'
