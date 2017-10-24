from nes.cpu.cycle import Cycle
from nes.cpu.microinstructions import CompareMicroinstruction
from .immediate_instruction import ImmediateInstruction
from .zeropage_instruction import ZeroPageInstruction
from .absolute_instruction import AbsoluteInstruction


class CpxImmediate(ImmediateInstruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([CompareMicroinstruction('X', 'DL')]))

    @property
    def name(self):
        return 'CPX'

    @property
    def opcode(self):
        return 0xE0

    @property
    def description(self):
        return 'Compare Memory and Index X'


class CpxZeroPage(ZeroPageInstruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([CompareMicroinstruction('X', 'DL')]))

    @property
    def name(self):
        return 'CPX'

    @property
    def opcode(self):
        return 0xE4

    @property
    def description(self):
        return 'Compare Memory and Index X'


class CpxAbsolute(AbsoluteInstruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([CompareMicroinstruction('X', 'DL')]))

    @property
    def name(self):
        return 'CPX'

    @property
    def opcode(self):
        return 0xEC

    @property
    def description(self):
        return 'Compare Memory and Index X'
