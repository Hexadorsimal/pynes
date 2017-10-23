from nes.cpu.cycle import Cycle
from nes.cpu.microinstructions import MoveMicroinstruction
from .zeropage_instruction import ZeroPageInstruction
from .zeropagey_instruction import ZeroPageYInstruction
from .absolute_instruction import AbsoluteInstruction


class StxZeroPage(ZeroPageInstruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([MoveMicroinstruction('X', 'DL')]))

    @property
    def name(self):
        return 'STX zpg'

    @property
    def opcode(self):
        return 0x86

    @property
    def description(self):
        return 'Store Index X in Memory (ZeroPage)'


class StxZeroPageY(ZeroPageYInstruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([MoveMicroinstruction('X', 'DL')]))

    @property
    def name(self):
        return 'STX zpg,Y'

    @property
    def opcode(self):
        return 0x96

    @property
    def description(self):
        return 'Store Index X in Memory (ZeroPageY)'


class StxAbsolute(AbsoluteInstruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([MoveMicroinstruction('X', 'DL')]))

    @property
    def name(self):
        return 'STX abs'

    @property
    def opcode(self):
        return 0x8E

    @property
    def description(self):
        return 'Store Index X in Memory (Absolute)'
