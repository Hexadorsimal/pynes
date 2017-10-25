from nes.cpu.cycle import Cycle
from nes.cpu.microinstructions import Branch
from ..addressing_modes import RelativeAddressing
from .instruction import Instruction


class Bvc(Instruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([Branch('V', False)]))
        self.addressing_modes = {
            0x50: RelativeAddressing
        }

    @property
    def name(self):
        return 'BVC'

    @property
    def description(self):
        return 'Branch on Overflow Clear'
