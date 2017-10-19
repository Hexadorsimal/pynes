from ..cycle import Cycle
from ..operation import MoveOperation
from ..zeropage_instruction import ZeroPageInstruction
from ..zeropagex_instruction import ZeroPageXInstruction
from ..absolute_instruction import AbsoluteInstruction
from ..absolutex_instruction import AbsoluteXInstruction
from ..absolutey_instruction import AbsoluteYInstruction
from ..indexed_indirect_instruction import IndexedIndirectInstruction
from ..indirect_indexed_instruction import IndirectIndexedInstruction


class StaZeroPage(ZeroPageInstruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([MoveOperation('A', 'DL')]))

    @property
    def name(self):
        return 'STA zpg'

    @property
    def opcode(self):
        return 0x85

    @property
    def description(self):
        return 'Store Accumulator in Memory (ZeroPage)'


class StaZeroPageX(ZeroPageXInstruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([MoveOperation('A', 'DL')]))

    @property
    def name(self):
        return 'STA zpg,X'

    @property
    def opcode(self):
        return 0x95

    @property
    def description(self):
        return 'Store Accumulator in Memory (ZeroPageX)'


class StaAbsolute(AbsoluteInstruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([MoveOperation('A', 'DL')]))

    @property
    def name(self):
        return 'STA abs'

    @property
    def opcode(self):
        return 0x8D

    @property
    def description(self):
        return 'Store Accumulator in Memory (Absolute)'


class StaAbsoluteX(AbsoluteXInstruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([MoveOperation('A', 'DL')]))

    @property
    def name(self):
        return 'STA abs,X'

    @property
    def opcode(self):
        return 0x9D

    @property
    def description(self):
        return 'Store Accumulator in Memory (AbsoluteX)'


class StaAbsoluteY(AbsoluteYInstruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([MoveOperation('A', 'DL')]))

    @property
    def name(self):
        return 'STA abs,Y'

    @property
    def opcode(self):
        return 0x99

    @property
    def description(self):
        return 'Store Accumulator in Memory (AbsoluteY)'


class StaIndexedIndirect(IndexedIndirectInstruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([MoveOperation('A', 'DL')]))

    @property
    def name(self):
        return 'STA (ind,X)'

    @property
    def opcode(self):
        return 0x81

    @property
    def description(self):
        return 'Store Accumulator in Memory (IndexedIndirect)'


class StaIndirectIndexed(IndirectIndexedInstruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([MoveOperation('A', 'DL')]))

    @property
    def name(self):
        return 'STA (ind),Y'

    @property
    def opcode(self):
        return 0x91

    @property
    def description(self):
        return 'Store Accumulator in Memory (IndirectIndexed)'
