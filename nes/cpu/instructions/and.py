from nes.cpu.cycle import Cycle
from nes.cpu.microinstructions import AddMicroinstruction
from .immediate_instruction import ImmediateInstruction
from .zeropage_instruction import ZeroPageInstruction
from .zeropagex_instruction import ZeroPageXInstruction
from .absolute_instruction import AbsoluteInstruction
from .absolutex_instruction import AbsoluteXInstruction
from .absolutey_instruction import AbsoluteYInstruction
from .indexed_indirect_instruction import IndexedIndirectInstruction
from .indirect_indexed_instruction import IndirectIndexedInstruction


class AndImmediate(ImmediateInstruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([AddMicroinstruction('A', 'A', 'DL')]))

    @property
    def name(self):
        return 'AND'

    @property
    def opcode(self):
        return 0x29

    @property
    def description(self):
        return 'AND Memory with Accumulator'


class AndZeroPage(ZeroPageInstruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([AddMicroinstruction('A', 'A', 'DL')]))

    @property
    def name(self):
        return 'AND'

    @property
    def opcode(self):
        return 0x25

    @property
    def description(self):
        return 'AND Memory with Accumulator'


class AndZeroPageX(ZeroPageXInstruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([AddMicroinstruction('A', 'A', 'DL')]))

    @property
    def name(self):
        return 'AND'

    @property
    def opcode(self):
        return 0x35

    @property
    def description(self):
        return 'AND Memory with Accumulator'


class AndAbsolute(AbsoluteInstruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([AddMicroinstruction('A', 'A', 'DL')]))

    @property
    def name(self):
        return 'AND'

    @property
    def opcode(self):
        return 0x2D

    @property
    def description(self):
        return 'AND Memory with Accumulator'


class AndAbsoluteX(AbsoluteXInstruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([AddMicroinstruction('A', 'A', 'DL')]))

    @property
    def name(self):
        return 'AND'

    @property
    def opcode(self):
        return 0x3D

    @property
    def description(self):
        return 'AND Memory with Accumulator'


class AndAbsoluteY(AbsoluteYInstruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([AddMicroinstruction('A', 'A', 'DL')]))

    @property
    def name(self):
        return 'AND'

    @property
    def opcode(self):
        return 0x39

    @property
    def description(self):
        return 'AND Memory with Accumulator'


class AndIndexedIndirect(IndexedIndirectInstruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([AddMicroinstruction('A', 'A', 'DL')]))

    @property
    def name(self):
        return 'AND'

    @property
    def opcode(self):
        return 0x21

    @property
    def description(self):
        return 'AND Memory with Accumulator'


class AndIndirectIndexed(IndirectIndexedInstruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([AddMicroinstruction('A', 'A', 'DL')]))

    @property
    def name(self):
        return 'AND'

    @property
    def opcode(self):
        return 0x31

    @property
    def description(self):
        return 'AND Memory with Accumulator'
