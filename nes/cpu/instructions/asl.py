from nes.cpu.cycle import Cycle
from nes.cpu.microinstructions import ArithmeticShiftLeftMicroinstruction
from .accumulator_instruction import AccumulatorInstruction
from .zeropage_instruction import ZeroPageInstruction
from .zeropagex_instruction import ZeroPageXInstruction
from .absolute_instruction import AbsoluteInstruction
from .absolutex_instruction import AbsoluteXInstruction


class AslAccumulator(AccumulatorInstruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([ArithmeticShiftLeftMicroinstruction('A', 'A')]))

    @property
    def name(self):
        return 'ASL'

    @property
    def opcode(self):
        return 0x0A

    @property
    def description(self):
        return 'Shift left One Bit (Memory or Accumulator)'


class AslZeroPage(ZeroPageInstruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([ArithmeticShiftLeftMicroinstruction('DL', 'DL')]))

    @property
    def name(self):
        return 'ASL'

    @property
    def opcode(self):
        return 0x06

    @property
    def description(self):
        return 'Shift left One Bit (Memory or Accumulator)'


class AslZeroPageX(ZeroPageXInstruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([ArithmeticShiftLeftMicroinstruction('DL', 'DL')]))

    @property
    def name(self):
        return 'ASL'

    @property
    def opcode(self):
        return 0x16

    @property
    def description(self):
        return 'Shift left One Bit (Memory or Accumulator)'


class AslAbsolute(AbsoluteInstruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([ArithmeticShiftLeftMicroinstruction('DL', 'DL')]))

    @property
    def name(self):
        return 'ASL'

    @property
    def opcode(self):
        return 0x0E

    @property
    def description(self):
        return 'Shift left One Bit (Memory or Accumulator)'


class AslAbsoluteX(AbsoluteXInstruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([ArithmeticShiftLeftMicroinstruction('DL', 'DL')]))

    @property
    def name(self):
        return 'ASL'

    @property
    def opcode(self):
        return 0x1E

    @property
    def description(self):
        return 'Shift left One Bit (Memory or Accumulator)'
