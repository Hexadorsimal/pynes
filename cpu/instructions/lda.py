from ..cycle import Cycle
from ..operation import MoveOperation
from ..immediate_instruction import ImmediateInstruction
from ..zeropage_instruction import ZeroPageInstruction
from ..zeropagex_instruction import ZeroPageXInstruction
from ..absolute_instruction import AbsoluteInstruction
from ..absolutex_instruction import AbsoluteXInstruction
from ..absolutey_instruction import AbsoluteYInstruction
from ..indexed_indirect_instruction import IndexedIndirectInstruction
from ..indirect_indexed_instruction import IndirectIndexedInstruction


class LdaImmediate(ImmediateInstruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([MoveOperation('DL', 'A')]))

    @property
    def name(self):
        return 'LDA #x'

    @property
    def opcode(self):
        return 0xA9

    @property
    def description(self):
        return 'Load Accumulator with Memory (Immediate)'


class LdaZeroPage(ZeroPageInstruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([MoveOperation('DL', 'A')]))

    @property
    def name(self):
        return 'LDA $00xx'

    @property
    def opcode(self):
        return 0xA5

    @property
    def description(self):
        return 'Load Accumulator with Memory (ZeroPage)'


class LdaZeroPageX(ZeroPageXInstruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([MoveOperation('DL', 'A')]))

    @property
    def name(self):
        return 'LDA 00,(xx)'

    @property
    def opcode(self):
        return 0xB5

    @property
    def description(self):
        return 'Load Accumulator with Memory (ZeroPageX)'


class LdaAbsolute(AbsoluteInstruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([MoveOperation('DL', 'A')]))

    @property
    def opcode(self):
        return 0xAD


class LdaAbsoluteX(AbsoluteXInstruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([MoveOperation('DL', 'A')]))

    @property
    def opcode(self):
        return 0xBD


class LdaAbsoluteY(AbsoluteYInstruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([MoveOperation('DL', 'A')]))

    @property
    def opcode(self):
        return 0xB9


class LdaIndexedIndirect(IndexedIndirectInstruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([MoveOperation('DL', 'A')]))

    @property
    def opcode(self):
        return 0xA1


class LdaIndirectIndexed(IndirectIndexedInstruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([MoveOperation('DL', 'A')]))

    @property
    def opcode(self):
        return 0xB1
