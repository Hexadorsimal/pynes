from nes.cpu.cycle import Cycle
from nes.cpu.microinstructions import Move
from ..addressing_modes import ImpliedAddressing
from .instruction import Instruction


class Tay(Instruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([Move('A', 'Y')]))
        self.addressing_modes = {
            0xAB: ImpliedAddressing
        }

    @property
    def name(self):
        return 'TAY'

    @property
    def description(self):
        return 'Transfer Accumulator to Index Y'
