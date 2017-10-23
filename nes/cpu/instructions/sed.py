from nes.cpu.cycle import Cycle
from nes.cpu.operations import SetFlagOperation
from .implied_instruction import ImpliedInstruction


class SetDecimalFlagOperation(SetFlagOperation):
    def __init__(self):
        super().__init__('D')


class Sed(ImpliedInstruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([SetDecimalFlagOperation()]))

    @property
    def name(self):
        return 'SED'

    @property
    def opcode(self):
        return 0xF8

    @property
    def description(self):
        return 'Set Decimal Mode'
