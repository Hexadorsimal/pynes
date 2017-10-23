from nes.cpu.cycle import Cycle
from nes.cpu.operations import IncrementOperation
from .implied_instruction import ImpliedInstruction


class Iny(ImpliedInstruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([IncrementOperation('Y')]))

    @property
    def name(self):
        return 'INY'

    @property
    def opcode(self):
        return 0xC8

    @property
    def description(self):
        return 'Increment Index Y by One'
