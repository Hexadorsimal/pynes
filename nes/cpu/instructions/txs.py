from nes.cpu.cycle import Cycle
from nes.cpu.operations import MoveOperation
from .implied_instruction import ImpliedInstruction


class Txs(ImpliedInstruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([MoveOperation('X', 'S')]))

    @property
    def name(self):
        return 'TXS'

    @property
    def opcode(self):
        return 0x9A

    @property
    def description(self):
        return 'Transfer Index X to Stack Pointer'
