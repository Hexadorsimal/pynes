from nes.cpu.cycle import Cycle
from nes.cpu.microinstructions import BitwiseXorMicroinstruction
from .immediate_instruction import ImmediateInstruction
from .zeropage_instruction import ZeroPageInstruction
from .zeropagex_instruction import ZeroPageXInstruction
from .absolute_instruction import AbsoluteInstruction
from .absolutex_instruction import AbsoluteXInstruction
from .absolutey_instruction import AbsoluteYInstruction
from .indexed_indirect_instruction import IndexedIndirectInstruction
from .indirect_indexed_instruction import IndirectIndexedInstruction


class EorImmediate(ImmediateInstruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([BitwiseXorMicroinstruction('A', 'A', 'DL')]))

    @property
    def name(self):
        return 'EOR'

    @property
    def opcode(self):
        return 0x49

    @property
    def description(self):
        return 'Exclusive OR Memory with Accumulator'


class EorZeroPage(ZeroPageInstruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([BitwiseXorMicroinstruction('A', 'A', 'DL')]))

    @property
    def name(self):
        return 'EOR'

    @property
    def opcode(self):
        return 0x45

    @property
    def description(self):
        return 'Exclusive OR Memory with Accumulator'


class EorZeroPageX(ZeroPageXInstruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([BitwiseXorMicroinstruction('A', 'A', 'DL')]))

    @property
    def name(self):
        return 'EOR'

    @property
    def opcode(self):
        return 0x55

    @property
    def description(self):
        return 'Exclusive OR Memory with Accumulator'


class EorAbsolute(AbsoluteInstruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([BitwiseXorMicroinstruction('A', 'A', 'DL')]))

    @property
    def name(self):
        return 'EOR'

    @property
    def opcode(self):
        return 0x4D

    @property
    def description(self):
        return 'Exclusive OR Memory with Accumulator'


class EorAbsoluteX(AbsoluteXInstruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([BitwiseXorMicroinstruction('A', 'A', 'DL')]))

    @property
    def name(self):
        return 'EOR'

    @property
    def opcode(self):
        return 0x5D

    @property
    def description(self):
        return 'Exclusive OR Memory with Accumulator'


class EorAbsoluteY(AbsoluteYInstruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([BitwiseXorMicroinstruction('A', 'A', 'DL')]))

    @property
    def name(self):
        return 'EOR'

    @property
    def opcode(self):
        return 0x59

    @property
    def description(self):
        return 'Exclusive OR Memory with Accumulator'


class EorIndexedIndirect(IndexedIndirectInstruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([BitwiseXorMicroinstruction('A', 'A', 'DL')]))

    @property
    def name(self):
        return 'EOR'

    @property
    def opcode(self):
        return 0x41

    @property
    def description(self):
        return 'Exclusive OR Memory with Accumulator'


class EorIndirectIndexed(IndirectIndexedInstruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([BitwiseXorMicroinstruction('A', 'A', 'DL')]))

    @property
    def name(self):
        return 'EOR'

    @property
    def opcode(self):
        return 0x51

    @property
    def description(self):
        return 'Exclusive OR Memory with Accumulator'
