from nes.cpu.cycle import Cycle
from nes.cpu.microinstructions import BitwiseOrMicroinstruction
from .immediate_instruction import ImmediateInstruction
from .zeropage_instruction import ZeroPageInstruction
from .zeropagex_instruction import ZeroPageXInstruction
from .absolute_instruction import AbsoluteInstruction
from .absolutex_instruction import AbsoluteXInstruction
from .absolutey_instruction import AbsoluteYInstruction
from .indexed_indirect_instruction import IndexedIndirectInstruction
from .indirect_indexed_instruction import IndirectIndexedInstruction


class OraImmediate(ImmediateInstruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([BitwiseOrMicroinstruction('A', 'A', 'DL')]))

    @property
    def name(self):
        return 'ORA'

    @property
    def opcode(self):
        return 0x09

    @property
    def description(self):
        return 'OR Memory with Accumulator'


class OraZeroPage(ZeroPageInstruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([BitwiseOrMicroinstruction('A', 'A', 'DL')]))

    @property
    def name(self):
        return 'ORA'

    @property
    def opcode(self):
        return 0x05

    @property
    def description(self):
        return 'OR Memory with Accumulator'


class OraZeroPageX(ZeroPageXInstruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([BitwiseOrMicroinstruction('A', 'A', 'DL')]))

    @property
    def name(self):
        return 'ORA'

    @property
    def opcode(self):
        return 0x15

    @property
    def description(self):
        return 'OR Memory with Accumulator'


class OraAbsolute(AbsoluteInstruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([BitwiseOrMicroinstruction('A', 'A', 'DL')]))

    @property
    def name(self):
        return 'ORA'

    @property
    def opcode(self):
        return 0x0D

    @property
    def description(self):
        return 'OR Memory with Accumulator'


class OraAbsoluteX(AbsoluteXInstruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([BitwiseOrMicroinstruction('A', 'A', 'DL')]))

    @property
    def name(self):
        return 'ORA'

    @property
    def opcode(self):
        return 0x1D

    @property
    def description(self):
        return 'OR Memory with Accumulator'


class OraAbsoluteY(AbsoluteYInstruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([BitwiseOrMicroinstruction('A', 'A', 'DL')]))

    @property
    def name(self):
        return 'ORA'

    @property
    def opcode(self):
        return 0x19

    @property
    def description(self):
        return 'OR Memory with Accumulator'


class OraIndexedIndirect(IndexedIndirectInstruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([BitwiseOrMicroinstruction('A', 'A', 'DL')]))

    @property
    def name(self):
        return 'ORA'

    @property
    def opcode(self):
        return 0x01

    @property
    def description(self):
        return 'OR Memory with Accumulator'


class OraIndirectIndexed(IndirectIndexedInstruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([BitwiseOrMicroinstruction('A', 'A', 'DL')]))

    @property
    def name(self):
        return 'ORA'

    @property
    def opcode(self):
        return 0x11

    @property
    def description(self):
        return 'OR Memory with Accumulator'
