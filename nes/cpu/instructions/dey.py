from nes.cpu.cycle import Cycle
from nes.cpu.microinstructions import DecrementMicroinstruction
from .implied_instruction import ImpliedInstruction


class Dey(ImpliedInstruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([DecrementMicroinstruction('Y')]))

    @property
    def name(self):
        return 'DEY'

    @property
    def opcode(self):
        return 0x88

    @property
    def description(self):
        return 'Decrement Index Y by One'
