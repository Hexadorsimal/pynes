from nes.cpu.cycle import Cycle
from nes.cpu.operations import MoveOperation
from .immediate_instruction import ImmediateInstruction
from .zeropage_instruction import ZeroPageInstruction
from .zeropagex_instruction import ZeroPageXInstruction
from .absolute_instruction import AbsoluteInstruction
from .absolutex_instruction import AbsoluteXInstruction


class LdyImmediate(ImmediateInstruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([MoveOperation('DL', 'Y')]))

    @property
    def name(self):
        return 'LDY #'

    @property
    def opcode(self):
        return 0xA0

    @property
    def description(self):
        return 'Load Index Y with Memory (Immediate)'


class LdyZeroPage(ZeroPageInstruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([MoveOperation('DL', 'Y')]))

    @property
    def name(self):
        return 'LDY zpg'

    @property
    def opcode(self):
        return 0xA4

    @property
    def description(self):
        return 'Load Index Y with Memory (ZeroPage)'


class LdyZeroPageX(ZeroPageXInstruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([MoveOperation('DL', 'Y')]))

    @property
    def name(self):
        return 'LDY zpg,X'

    @property
    def opcode(self):
        return 0xB4

    @property
    def description(self):
        return 'Load Index Y with Memory (ZeroPageX)'


class LdyAbsolute(AbsoluteInstruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([MoveOperation('DL', 'Y')]))

    @property
    def name(self):
        return 'LDY abs'

    @property
    def opcode(self):
        return 0xAC

    @property
    def description(self):
        return 'Load Index Y with Memory (Absolute)'


class LdyAbsoluteX(AbsoluteXInstruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([MoveOperation('DL', 'Y')]))

    @property
    def name(self):
        return 'LDY abs,X'

    @property
    def opcode(self):
        return 0xBC

    @property
    def description(self):
        return 'Load Index Y with Memory (AbsoluteX)'
