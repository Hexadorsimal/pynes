from nes.cpu.cycle import Cycle
from nes.cpu.microinstructions import Branch
from ..addressing_modes import RelativeAddressing
from .instruction import Instruction


class Beq(Instruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([Branch('Z', True)]))
        self.addressing_modes = {
            0xF0: RelativeAddressing
        }

    @property
    def name(self):
        return 'BEQ'

    @property
    def description(self):
        return 'Branch on Result Zero'
