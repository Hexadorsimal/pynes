from nes.cpu.cycle import Cycle
from nes.cpu.microinstructions import Microinstruction
from .implied_instruction import ImpliedInstruction


class BreakMicroinstruction(Microinstruction):
    def __init__(self):
        super().__init__()

    def execute(self, processor):
        pass


class Brk(ImpliedInstruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([BreakMicroinstruction()]))

    @property
    def name(self):
        return 'BRK'

    @property
    def opcode(self):
        return 0x00

    @property
    def description(self):
        return 'Force Break'
