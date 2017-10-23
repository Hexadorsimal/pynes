from nes.cpu.cycle import Cycle
from nes.cpu.microinstructions import SetFlagMicroinstruction
from .implied_instruction import ImpliedInstruction


class SetInterruptDisableBitOperation(SetFlagMicroinstruction):
    def __init__(self):
        super().__init__('I')


class Sei(ImpliedInstruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([SetInterruptDisableBitOperation()]))

    @property
    def name(self):
        return 'SEI'

    @property
    def opcode(self):
        return 0x78

    @property
    def description(self):
        return 'Set Interrupt Disable Status'
