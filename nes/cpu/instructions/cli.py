from nes.cpu.cycle import Cycle
from nes.cpu.operations import ClearFlagOperation
from .implied_instruction import ImpliedInstruction


class ClearInterruptDisableBitOperation(ClearFlagOperation):
    def __init__(self):
        super().__init__('I')


class Cli(ImpliedInstruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([ClearInterruptDisableBitOperation()]))

    @property
    def name(self):
        return 'CLI'

    @property
    def opcode(self):
        return 0x58

    @property
    def description(self):
        return 'Clear Interrupt Disable Bit'
