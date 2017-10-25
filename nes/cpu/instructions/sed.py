from nes.cpu.cycle import Cycle
from nes.cpu.microinstructions import SetFlag
from ..addressing_modes import ImpliedAddressing
from .instruction import Instruction


class Sed(Instruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([SetFlag('D')]))
        self.addressing_modes = {
            0xF8: ImpliedAddressing
        }

    @property
    def name(self):
        return 'SED'

    @property
    def description(self):
        return 'Set Decimal Mode'
