from nes.cpu.cycle import Cycle
from nes.cpu.microinstructions import Move
from ..addressing_modes import ImpliedAddressing
from .instruction import Instruction


class Txa(Instruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([Move('X', 'A')]))
        self.addressing_modes = {
            0x8A: ImpliedAddressing
        }

    @property
    def name(self):
        return 'TXA'

    @property
    def description(self):
        return 'Transfer Index X to Accumulator'
