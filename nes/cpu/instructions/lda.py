from nes.cpu.cycle import Cycle
from nes.cpu.operations import MoveOperation
from .immediate_instruction import ImmediateInstruction
from .zeropage_instruction import ZeroPageInstruction
from .zeropagex_instruction import ZeroPageXInstruction
from .absolute_instruction import AbsoluteInstruction
from .absolutex_instruction import AbsoluteXInstruction
from .absolutey_instruction import AbsoluteYInstruction
from .indexed_indirect_instruction import IndexedIndirectInstruction
from .indirect_indexed_instruction import IndirectIndexedInstruction


class LdaImmediate(ImmediateInstruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([MoveOperation('DL', 'A')]))

    @property
    def name(self):
        return 'LDA #'

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
        return 'LDA zpg'

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
        return 'LDA zpg,X'

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
    def name(self):
        return 'LDA abs'

    @property
    def opcode(self):
        return 0xAD

    @property
    def description(self):
        return 'Load Accumulator with Memory (Absolute)'


class LdaAbsoluteX(AbsoluteXInstruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([MoveOperation('DL', 'A')]))

    @property
    def name(self):
        return 'LDA abs,X'

    @property
    def opcode(self):
        return 0xBD

    @property
    def description(self):
        return 'Load Accumulator with Memory (AbsoluteX)'


class LdaAbsoluteY(AbsoluteYInstruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([MoveOperation('DL', 'A')]))

    @property
    def name(self):
        return 'LDA abs,Y'

    @property
    def opcode(self):
        return 0xB9

    @property
    def description(self):
        return 'Load Accumulator with Memory (AbsoluteY)'


class LdaIndexedIndirect(IndexedIndirectInstruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([MoveOperation('DL', 'A')]))

    @property
    def name(self):
        return 'LDA (ind,X)'

    @property
    def opcode(self):
        return 0xA1

    @property
    def description(self):
        return 'Load Accumulator with Memory (IndexedIndirect)'


class LdaIndirectIndexed(IndirectIndexedInstruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([MoveOperation('DL', 'A')]))

    @property
    def name(self):
        return 'LDA (ind),Y'

    @property
    def opcode(self):
        return 0xB1

    @property
    def description(self):
        return 'Load Accumulator with Memory (IndirectIndexed)'
