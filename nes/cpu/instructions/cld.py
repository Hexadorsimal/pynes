from nes.cpu.cycle import Cycle
from nes.cpu.microinstructions import ClearFlag
from ..addressing_modes import ImpliedAddressing
from .instruction import Instruction


class Cld(Instruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([ClearFlag('D')]))
        self.addressing_modes = {
            0xD8: ImpliedAddressing
        }

    @property
    def name(self):
        return 'CLD'

    @property
    def description(self):
        return 'Clear Decimal Mode'
