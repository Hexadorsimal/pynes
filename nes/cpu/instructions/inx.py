from nes.cpu.cycle import Cycle
from nes.cpu.microinstructions import IncrementMicroinstruction
from .implied_instruction import ImpliedInstruction


class Inx(ImpliedInstruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([IncrementMicroinstruction('X')]))

    @property
    def name(self):
        return 'INX'

    @property
    def opcode(self):
        return 0xE8

    @property
    def description(self):
        return 'Increment Index X by One'
