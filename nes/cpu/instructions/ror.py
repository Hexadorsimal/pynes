from nes.cpu.cycle import Cycle
from nes.cpu.microinstructions import RotateRightMicroinstruction
from .accumulator_instruction import AccumulatorInstruction
from .zeropage_instruction import ZeroPageInstruction
from .zeropagex_instruction import ZeroPageXInstruction
from .absolute_instruction import AbsoluteInstruction
from .absolutex_instruction import AbsoluteXInstruction


class RorAccumulator(AccumulatorInstruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([RotateRightMicroinstruction('A', 'A')]))

    @property
    def name(self):
        return 'ROR'

    @property
    def opcode(self):
        return 0x6A

    @property
    def description(self):
        return 'Rotate One Bit Right (Memory or Accumulator)'


class RorZeroPage(ZeroPageInstruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([RotateRightMicroinstruction('DL', 'DL')]))

    @property
    def name(self):
        return 'ROR'

    @property
    def opcode(self):
        return 0x66

    @property
    def description(self):
        return 'Rotate One Bit Right (Memory or Accumulator)'


class RorZeroPageX(ZeroPageXInstruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([RotateRightMicroinstruction('DL', 'DL')]))

    @property
    def name(self):
        return 'ROR'

    @property
    def opcode(self):
        return 0x76

    @property
    def description(self):
        return 'Rotate One Bit Right (Memory or Accumulator)'


class RorAbsolute(AbsoluteInstruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([RotateRightMicroinstruction('DL', 'DL')]))

    @property
    def name(self):
        return 'ROR'

    @property
    def opcode(self):
        return 0x6E

    @property
    def description(self):
        return 'Rotate One Bit Right (Memory or Accumulator)'


class RorAbsoluteX(AbsoluteXInstruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([RotateRightMicroinstruction('DL', 'DL')]))

    @property
    def name(self):
        return 'ROR'

    @property
    def opcode(self):
        return 0x7E

    @property
    def description(self):
        return 'Rotate One Bit Right (Memory or Accumulator)'
