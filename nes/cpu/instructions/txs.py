from nes.cpu.cycle import Cycle
from nes.cpu.microinstructions import Move
from ..addressing_modes import ImpliedAddressing
from .instruction import Instruction


class Txs(Instruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([Move('X', 'S')]))
        self.addressing_modes = {
            0x9A: ImpliedAddressing
        }

    @property
    def name(self):
        return 'TXS'

    @property
    def description(self):
        return 'Transfer Index X to Stack Pointer'
