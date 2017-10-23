from ..alu.alu_operations import AluIncrementOperation
from ..cycle import Cycle
from ..implied_instruction import ImpliedInstruction


class Iny(ImpliedInstruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([AluIncrementOperation('Y')]))

    @property
    def name(self):
        return 'INY'

    @property
    def opcode(self):
        return 0xC8

    @property
    def description(self):
        return 'Increment Index Y by One'
