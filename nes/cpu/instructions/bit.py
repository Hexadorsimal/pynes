from nes.cpu.cycle import Cycle
from nes.cpu.microinstructions import BitTestMicroinstruction
from .zeropage_instruction import ZeroPageInstruction
from .absolute_instruction import AbsoluteInstruction


class BitZeroPage(ZeroPageInstruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([BitTestMicroinstruction('A', 'DL')]))

    @property
    def name(self):
        return 'BIT'

    @property
    def opcode(self):
        return 0x24

    @property
    def description(self):
        return 'Test Bits in Memory with Accumulator'


class BitAbsolute(AbsoluteInstruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([BitTestMicroinstruction('A', 'DL')]))

    @property
    def name(self):
        return 'BIT'

    @property
    def opcode(self):
        return 0x2C

    @property
    def description(self):
        return 'Test Bits in Memory with Accumulator'
