from ..cycle import Cycle
from ..operation import MoveOperation
from ..zeropage_instruction import ZeroPageInstruction
from ..zeropagex_instruction import ZeroPageXInstruction
from ..absolute_instruction import AbsoluteInstruction


class StyZeroPage(ZeroPageInstruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([MoveOperation('Y', 'DL')]))

    @property
    def name(self):
        return 'STY zpg'

    @property
    def opcode(self):
        return 0x84

    @property
    def description(self):
        return 'Store Index Y in Memory (ZeroPage)'


class StyZeroPageX(ZeroPageXInstruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([MoveOperation('Y', 'DL')]))

    @property
    def name(self):
        return 'STY zpg,X'

    @property
    def opcode(self):
        return 0x94

    @property
    def description(self):
        return 'Store Index Y in Memory (ZeroPageX)'


class StyAbsolute(AbsoluteInstruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([MoveOperation('Y', 'DL')]))

    @property
    def name(self):
        return 'STY abs'

    @property
    def opcode(self):
        return 0x8C

    @property
    def description(self):
        return 'Store Index Y in Memory (Absolute)'
