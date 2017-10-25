from nes.cpu.cycle import Cycle
from nes.cpu.microinstructions import Branch
from ..addressing_modes import RelativeAddressing
from .instruction import Instruction


class Bcs(Instruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([Branch('C', True)]))
        self.addressing_modes = {
            0x80: RelativeAddressing
        }

    @property
    def name(self):
        return 'BCS'

    @property
    def description(self):
        return 'Branch on Carry Set'
