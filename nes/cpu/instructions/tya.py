from nes.cpu.cycle import Cycle
from nes.cpu.microinstructions import Move
from ..addressing_modes import ImpliedAddressing
from .instruction import Instruction


class Tya(Instruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([Move('Y', 'A')]))
        self.addressing_modes = {
            0x98: ImpliedAddressing
        }

    @property
    def name(self):
        return 'TYA'

    @property
    def description(self):
        return 'Transfer Index Y to Accumulator'
