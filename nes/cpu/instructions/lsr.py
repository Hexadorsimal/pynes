from nes.cpu.cycle import Cycle
from nes.cpu.microinstructions import LogicalShiftRightMicroinstruction
from .accumulator_instruction import AccumulatorInstruction
from .zeropage_instruction import ZeroPageInstruction
from .zeropagex_instruction import ZeroPageXInstruction
from .absolute_instruction import AbsoluteInstruction
from .absolutex_instruction import AbsoluteXInstruction


class LsrAccumulator(AccumulatorInstruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([LogicalShiftRightMicroinstruction('A', 'A')]))

    @property
    def name(self):
        return 'LSR'

    @property
    def opcode(self):
        return 0x4A

    @property
    def description(self):
        return 'Shift One Bit Right (Memory or Accumulator)'


class LsrZeroPage(ZeroPageInstruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([LogicalShiftRightMicroinstruction('DL', 'DL')]))

    @property
    def name(self):
        return 'LSR'

    @property
    def opcode(self):
        return 0x46

    @property
    def description(self):
        return 'Shift One Bit Right (Memory or Accumulator)'


class LsrZeroPageX(ZeroPageXInstruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([LogicalShiftRightMicroinstruction('DL', 'DL')]))

    @property
    def name(self):
        return 'LSR'

    @property
    def opcode(self):
        return 0x56

    @property
    def description(self):
        return 'Shift One Bit Right (Memory or Accumulator)'


class LsrAbsolute(AbsoluteInstruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([LogicalShiftRightMicroinstruction('DL', 'DL')]))

    @property
    def name(self):
        return 'LSR'

    @property
    def opcode(self):
        return 0x4E

    @property
    def description(self):
        return 'Shift One Bit Right (Memory or Accumulator)'


class LsrAbsoluteX(AbsoluteXInstruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([LogicalShiftRightMicroinstruction('DL', 'DL')]))

    @property
    def name(self):
        return 'LSR'

    @property
    def opcode(self):
        return 0x5E

    @property
    def description(self):
        return 'Shift One Bit Right (Memory or Accumulator)'
