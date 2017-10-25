from nes.cpu.cycle import Cycle
from nes.cpu.microinstructions import ClearFlag
from ..addressing_modes import ImpliedAddressing
from .instruction import Instruction


class Clv(Instruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([ClearFlag('V')]))
        self.addressing_modes = {
            0xB8: ImpliedAddressing
        }

    @property
    def name(self):
        return 'CLV'

    @property
    def description(self):
        return 'Clear Overflow Flag'
