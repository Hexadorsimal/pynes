from ..alu.alu_operations import AluDecrementOperation
from ..cycle import Cycle
from ..implied_instruction import ImpliedInstruction


class Dey(ImpliedInstruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([AluDecrementOperation('Y')]))

    @property
    def name(self):
        return 'DEY'

    @property
    def opcode(self):
        return 0x88

    @property
    def description(self):
        return 'Decrement Index Y by One'
