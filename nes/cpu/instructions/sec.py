from nes.cpu.cycle import Cycle
from nes.cpu.microinstructions import SetFlag
from ..addressing_modes import ImpliedAddressing
from .instruction import Instruction


class Sec(Instruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([SetFlag('C')]))
        self.addressing_modes = {
            0x38: ImpliedAddressing
        }

    @property
    def name(self):
        return 'SEC'

    @property
    def description(self):
        return 'Set Carry Flag'
