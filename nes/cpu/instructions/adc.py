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


class AdcImmediate(ImmediateInstruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([AddMicroinstruction('A', 'A', 'DL')]))

    @property
    def name(self):
        return 'ADC'

    @property
    def opcode(self):
        return 0x69

    @property
    def description(self):
        return 'Add Memory to Accumulator with Carry'


class AdcZeroPage(ZeroPageInstruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([AddMicroinstruction('A', 'A', 'DL')]))

    @property
    def name(self):
        return 'ADC'

    @property
    def opcode(self):
        return 0x65

    @property
    def description(self):
        return 'Add Memory to Accumulator with Carry'


class AdcZeroPageX(ZeroPageXInstruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([AddMicroinstruction('A', 'A', 'DL')]))

    @property
    def name(self):
        return 'ADC'

    @property
    def opcode(self):
        return 0x75

    @property
    def description(self):
        return 'Add Memory to Accumulator with Carry'


class AdcAbsolute(AbsoluteInstruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([AddMicroinstruction('A', 'A', 'DL')]))

    @property
    def name(self):
        return 'ADC'

    @property
    def opcode(self):
        return 0x6D

    @property
    def description(self):
        return 'Add Memory to Accumulator with Carry'


class AdcAbsoluteX(AbsoluteXInstruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([AddMicroinstruction('A', 'A', 'DL')]))

    @property
    def name(self):
        return 'ADC'

    @property
    def opcode(self):
        return 0x7D

    @property
    def description(self):
        return 'Add Memory to Accumulator with Carry'


class AdcAbsoluteY(AbsoluteYInstruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([AddMicroinstruction('A', 'A', 'DL')]))

    @property
    def name(self):
        return 'ADC'

    @property
    def opcode(self):
        return 0x79

    @property
    def description(self):
        return 'Add Memory to Accumulator with Carry'


class AdcIndexedIndirect(IndexedIndirectInstruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([AddMicroinstruction('A', 'A', 'DL')]))

    @property
    def name(self):
        return 'ADC'

    @property
    def opcode(self):
        return 0x61

    @property
    def description(self):
        return 'Add Memory to Accumulator with Carry'


class AdcIndirectIndexed(IndirectIndexedInstruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([AddMicroinstruction('A', 'A', 'DL')]))

    @property
    def name(self):
        return 'ADC'

    @property
    def opcode(self):
        return 0x71

    @property
    def description(self):
        return 'Add Memory to Accumulator with Carry'
