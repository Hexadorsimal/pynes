from nes.cpu.cycle import Cycle
from nes.cpu.microinstructions import CompareMicroinstruction
from .immediate_instruction import ImmediateInstruction
from .zeropage_instruction import ZeroPageInstruction
from .zeropagex_instruction import ZeroPageXInstruction
from .absolute_instruction import AbsoluteInstruction
from .absolutex_instruction import AbsoluteXInstruction
from .absolutey_instruction import AbsoluteYInstruction
from .indexed_indirect_instruction import IndexedIndirectInstruction
from .indirect_indexed_instruction import IndirectIndexedInstruction


class CmpImmediate(ImmediateInstruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([CompareMicroinstruction('A', 'DL')]))

    @property
    def name(self):
        return 'CMP'

    @property
    def opcode(self):
        return 0xC9

    @property
    def description(self):
        return 'Compare Memory and Accumulator'


class CmpZeroPage(ZeroPageInstruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([CompareMicroinstruction('A', 'DL')]))

    @property
    def name(self):
        return 'CMP'

    @property
    def opcode(self):
        return 0xC5

    @property
    def description(self):
        return 'Compare Memory and Accumulator'


class CmpZeroPageX(ZeroPageXInstruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([CompareMicroinstruction('A', 'DL')]))

    @property
    def name(self):
        return 'CMP'

    @property
    def opcode(self):
        return 0xD5

    @property
    def description(self):
        return 'Compare Memory and Accumulator'


class CmpAbsolute(AbsoluteInstruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([CompareMicroinstruction('A', 'DL')]))

    @property
    def name(self):
        return 'CMP'

    @property
    def opcode(self):
        return 0xCD

    @property
    def description(self):
        return 'Compare Memory and Accumulator'


class CmpAbsoluteX(AbsoluteXInstruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([CompareMicroinstruction('A', 'DL')]))

    @property
    def name(self):
        return 'CMP'

    @property
    def opcode(self):
        return 0xDD

    @property
    def description(self):
        return 'Compare Memory and Accumulator'


class CmpAbsoluteY(AbsoluteYInstruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([CompareMicroinstruction('A', 'DL')]))

    @property
    def name(self):
        return 'CMP'

    @property
    def opcode(self):
        return 0xD9

    @property
    def description(self):
        return 'Compare Memory and Accumulator'


class CmpIndexedIndirect(IndexedIndirectInstruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([CompareMicroinstruction('A', 'DL')]))

    @property
    def name(self):
        return 'CMP'

    @property
    def opcode(self):
        return 0xC1

    @property
    def description(self):
        return 'Compare Memory and Accumulator'


class CmpIndirectIndexed(IndirectIndexedInstruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([CompareMicroinstruction('A', 'DL')]))

    @property
    def name(self):
        return 'CMP'

    @property
    def opcode(self):
        return 0xD1

    @property
    def description(self):
        return 'Compare Memory and Accumulator'
