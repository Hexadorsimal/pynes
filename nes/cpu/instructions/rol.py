from nes.cpu.cycle import Cycle
from nes.cpu.microinstructions import RotateLeftMicroinstruction
from .accumulator_instruction import AccumulatorInstruction
from .zeropage_instruction import ZeroPageInstruction
from .zeropagex_instruction import ZeroPageXInstruction
from .absolute_instruction import AbsoluteInstruction
from .absolutex_instruction import AbsoluteXInstruction


class RolAccumulator(AccumulatorInstruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([RotateLeftMicroinstruction('A', 'A')]))

    @property
    def name(self):
        return 'ROL'

    @property
    def opcode(self):
        return 0x2A

    @property
    def description(self):
        return 'Rotate One Bit Left (Memory or Accumulator)'


class RolZeroPage(ZeroPageInstruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([RotateLeftMicroinstruction('DL', 'DL')]))

    @property
    def name(self):
        return 'ROL'

    @property
    def opcode(self):
        return 0x26

    @property
    def description(self):
        return 'Rotate One Bit Left (Memory or Accumulator)'


class RolZeroPageX(ZeroPageXInstruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([RotateLeftMicroinstruction('DL', 'DL')]))

    @property
    def name(self):
        return 'ROL'

    @property
    def opcode(self):
        return 0x36

    @property
    def description(self):
        return 'Rotate One Bit Left (Memory or Accumulator)'


class RolAbsolute(AbsoluteInstruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([RotateLeftMicroinstruction('DL', 'DL')]))

    @property
    def name(self):
        return 'ROL'

    @property
    def opcode(self):
        return 0x2E

    @property
    def description(self):
        return 'Rotate One Bit Left (Memory or Accumulator)'


class RolAbsoluteX(AbsoluteXInstruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([RotateLeftMicroinstruction('DL', 'DL')]))

    @property
    def name(self):
        return 'ROL'

    @property
    def opcode(self):
        return 0x3E

    @property
    def description(self):
        return 'Rotate One Bit Left (Memory or Accumulator)'
