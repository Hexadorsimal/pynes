from nes.cpu.cycle import Cycle
from nes.cpu.microinstructions import SubtractMicroinstruction
from .immediate_instruction import ImmediateInstruction
from .zeropage_instruction import ZeroPageInstruction
from .zeropagex_instruction import ZeroPageXInstruction
from .absolute_instruction import AbsoluteInstruction
from .absolutex_instruction import AbsoluteXInstruction
from .absolutey_instruction import AbsoluteYInstruction
from .indexed_indirect_instruction import IndexedIndirectInstruction
from .indirect_indexed_instruction import IndirectIndexedInstruction


class SbcImmediate(ImmediateInstruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([SubtractMicroinstruction('A', 'A', 'DL')]))

    @property
    def name(self):
        return 'SBC'

    @property
    def opcode(self):
        return 0xE9

    @property
    def description(self):
        return 'Subtract Memory from Accumulator with Borrow'


class SbcZeroPage(ZeroPageInstruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([SubtractMicroinstruction('A', 'A', 'DL')]))

    @property
    def name(self):
        return 'SBC'

    @property
    def opcode(self):
        return 0xE5

    @property
    def description(self):
        return 'Subtract Memory from Accumulator with Borrow'


class SbcZeroPageX(ZeroPageXInstruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([SubtractMicroinstruction('A', 'A', 'DL')]))

    @property
    def name(self):
        return 'SBC'

    @property
    def opcode(self):
        return 0xF5

    @property
    def description(self):
        return 'Subtract Memory from Accumulator with Borrow'


class SbcAbsolute(AbsoluteInstruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([SubtractMicroinstruction('A', 'A', 'DL')]))

    @property
    def name(self):
        return 'SBC'

    @property
    def opcode(self):
        return 0xED

    @property
    def description(self):
        return 'Subtract Memory from Accumulator with Borrow'


class SbcAbsoluteX(AbsoluteXInstruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([SubtractMicroinstruction('A', 'A', 'DL')]))

    @property
    def name(self):
        return 'SBC'

    @property
    def opcode(self):
        return 0xFD

    @property
    def description(self):
        return 'Subtract Memory from Accumulator with Borrow'


class SbcAbsoluteY(AbsoluteYInstruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([SubtractMicroinstruction('A', 'A', 'DL')]))

    @property
    def name(self):
        return 'SBC'

    @property
    def opcode(self):
        return 0xF9

    @property
    def description(self):
        return 'Subtract Memory from Accumulator with Borrow'


class SbcIndexedIndirect(IndexedIndirectInstruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([SubtractMicroinstruction('A', 'A', 'DL')]))

    @property
    def name(self):
        return 'SBC'

    @property
    def opcode(self):
        return 0xE1

    @property
    def description(self):
        return 'Subtract Memory from Accumulator with Borrow'


class SbcIndirectIndexed(IndirectIndexedInstruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([SubtractMicroinstruction('A', 'A', 'DL')]))

    @property
    def name(self):
        return 'SBC'

    @property
    def opcode(self):
        return 0xF1

    @property
    def description(self):
        return 'Subtract Memory from Accumulator with Borrow'
