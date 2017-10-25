from nes.cpu.cycle import Cycle
from nes.cpu.microinstructions import SetFlag
from ..addressing_modes import ImpliedAddressing
from .instruction import Instruction


class Sei(Instruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([SetFlag('I')]))
        self.addressing_modes = {
            0x78: ImpliedAddressing
        }

    @property
    def name(self):
        return 'SEI'

    @property
    def description(self):
        return 'Set Interrupt Disable Status'
