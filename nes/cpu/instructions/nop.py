from nes.cpu.cycle import Cycle
from nes.cpu.operations import Operation
from .implied_instruction import ImpliedInstruction


class NopOperation(Operation):
    def __init__(self):
        super().__init__()

    def execute(self, processor):
        pass


class Nop(ImpliedInstruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([NopOperation()]))

    @property
    def name(self):
        return 'NOP'

    @property
    def opcode(self):
        return 0xEA

    @property
    def description(self):
        return 'No Operation'
