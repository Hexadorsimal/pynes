from nes.cpu.cycle import Cycle
from nes.cpu.microinstructions import Branch
from ..addressing_modes import RelativeAddressing
from .instruction import Instruction


class Bmi(Instruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([Branch('N', True)]))
        self.addressing_modes = {
            0x30: RelativeAddressing
        }

    @property
    def name(self):
        return 'BMI'

    @property
    def description(self):
        return 'Branch on Result Minus'
