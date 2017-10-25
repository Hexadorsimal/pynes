from nes.cpu.cycle import Cycle
from nes.cpu.microinstructions import Branch
from ..addressing_modes import RelativeAddressing
from .instruction import Instruction


class Bcc(Instruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([Branch('C', False)]))
        self.addressing_modes = {
            0x90: RelativeAddressing
        }

    @property
    def name(self):
        return 'BCC'

    @property
    def description(self):
        return 'Branch on Carry Clear'
