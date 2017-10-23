from nes.cpu.cycle import Cycle
from nes.cpu.microinstructions import DecrementMicroinstruction
from .implied_instruction import ImpliedInstruction


class Dex(ImpliedInstruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([DecrementMicroinstruction('X')]))

    @property
    def name(self):
        return 'DEX'

    @property
    def opcode(self):
        return 0xCA

    @property
    def description(self):
        return 'Decrement Index X by One'
