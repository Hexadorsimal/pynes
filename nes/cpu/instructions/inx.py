from nes.cpu.cycle import Cycle
from nes.cpu.operations import IncrementOperation
from .implied_instruction import ImpliedInstruction


class Inx(ImpliedInstruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([IncrementOperation('X')]))

    @property
    def name(self):
        return 'INX'

    @property
    def opcode(self):
        return 0xE8

    @property
    def description(self):
        return 'Increment Index X by One'
