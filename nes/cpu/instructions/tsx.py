from nes.cpu.cycle import Cycle
from nes.cpu.microinstructions import Move
from ..addressing_modes import ImpliedAddressing
from .instruction import Instruction


class Tsx(Instruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([Move('S', 'X')]))
        self.addressing_modes = {
            0xBA: ImpliedAddressing
        }

    @property
    def name(self):
        return 'TSX'

    @property
    def description(self):
        return 'Transfer Stack Pointer to Index X'
