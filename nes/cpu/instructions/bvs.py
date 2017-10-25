from nes.cpu.cycle import Cycle
from nes.cpu.microinstructions import Branch
from ..addressing_modes import RelativeAddressing
from .instruction import Instruction


class Bvs(Instruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([Branch('V', True)]))
        self.addressing_modes = {
            0x70: RelativeAddressing
        }

    @property
    def name(self):
        return 'BVS'

    @property
    def description(self):
        return 'Branch on Overflow Set'
