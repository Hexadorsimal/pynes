from nes.cpu.cycle import Cycle
from nes.cpu.microinstructions import MoveMicroinstruction
from .immediate_instruction import ImmediateInstruction
from .zeropage_instruction import ZeroPageInstruction
from .zeropagey_instruction import ZeroPageYInstruction
from .absolute_instruction import AbsoluteInstruction
from .absolutey_instruction import AbsoluteYInstruction


class LdxImmediate(ImmediateInstruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([MoveMicroinstruction('DL', 'X')]))

    @property
    def name(self):
        return 'LDX #'

    @property
    def opcode(self):
        return 0xA2

    @property
    def description(self):
        return 'Load Index X with Memory (Immediate)'


class LdxZeroPage(ZeroPageInstruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([MoveMicroinstruction('DL', 'X')]))

    @property
    def name(self):
        return 'LDX zpg'

    @property
    def opcode(self):
        return 0xA6

    @property
    def description(self):
        return 'Load Index X with Memory (ZeroPage)'


class LdxZeroPageY(ZeroPageYInstruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([MoveMicroinstruction('DL', 'X')]))

    @property
    def name(self):
        return 'LDX zpg,Y'

    @property
    def opcode(self):
        return 0xB6

    @property
    def description(self):
        return 'Load Index X with Memory (ZeroPageY)'


class LdxAbsolute(AbsoluteInstruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([MoveMicroinstruction('DL', 'X')]))

    @property
    def name(self):
        return 'LDX abs'

    @property
    def opcode(self):
        return 0xAE

    @property
    def description(self):
        return 'Load Index X with Memory (Absolute)'


class LdxAbsoluteY(AbsoluteYInstruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([MoveMicroinstruction('DL', 'X')]))

    @property
    def name(self):
        return 'LDX abs,Y'

    @property
    def opcode(self):
        return 0xBE

    @property
    def description(self):
        return 'Load Index X with Memory (AbsoluteY)'
