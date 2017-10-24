from nes.cpu.cycle import Cycle
from nes.cpu.microinstructions import CompareMicroinstruction
from .immediate_instruction import ImmediateInstruction
from .zeropage_instruction import ZeroPageInstruction
from .absolute_instruction import AbsoluteInstruction


class CpyImmediate(ImmediateInstruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([CompareMicroinstruction('Y', 'DL')]))

    @property
    def name(self):
        return 'CPY'

    @property
    def opcode(self):
        return 0xC0

    @property
    def description(self):
        return 'Compare Memory and Index Y'


class CpyZeroPage(ZeroPageInstruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([CompareMicroinstruction('Y', 'DL')]))

    @property
    def name(self):
        return 'CPY'

    @property
    def opcode(self):
        return 0xC4

    @property
    def description(self):
        return 'Compare Memory and Index Y'


class CpyAbsolute(AbsoluteInstruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([CompareMicroinstruction('Y', 'DL')]))

    @property
    def name(self):
        return 'CPY'

    @property
    def opcode(self):
        return 0xCC

    @property
    def description(self):
        return 'Compare Memory and Index Y'
