from nes.cpu.cycle import Cycle
from nes.cpu.microinstructions import ClearFlagMicroinstruction
from .implied_instruction import ImpliedInstruction


class ClearOverflowFlagOperation(ClearFlagMicroinstruction):
    def __init__(self):
        super().__init__('I')


class Clv(ImpliedInstruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([ClearOverflowFlagOperation()]))

    @property
    def name(self):
        return 'CLV'

    @property
    def opcode(self):
        return 0xB8

    @property
    def description(self):
        return 'Clear Overflow Flag'
