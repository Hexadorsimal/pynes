from nes.cpu.cycle import Cycle
from nes.cpu.microinstructions import Move
from ..addressing_modes import ImpliedAddressing
from .instruction import Instruction


class Tax(Instruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([Move('A', 'X')]))
        self.addressing_modes = {
            0xAA: ImpliedAddressing
        }

    @property
    def name(self):
        return 'TAX'

    @property
    def description(self):
        return 'Transfer Accumulator to Index X'
