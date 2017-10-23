from nes.cpu.cycle import Cycle
from nes.cpu.microinstructions import IncrementMicroinstruction
from .zeropage_instruction import ZeroPageInstruction
from .zeropagex_instruction import ZeroPageXInstruction
from .absolute_instruction import AbsoluteInstruction
from .absolutex_instruction import AbsoluteXInstruction


class IncZeroPage(ZeroPageInstruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([IncrementMicroinstruction('DL')]))

    @property
    def name(self):
        return 'INC'

    @property
    def opcode(self):
        return 0xE6

    @property
    def description(self):
        return 'Increment Memory by One'


class IncZeroPageX(ZeroPageXInstruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([IncrementMicroinstruction('DL')]))

    @property
    def name(self):
        return 'INC'

    @property
    def opcode(self):
        return 0xF6

    @property
    def description(self):
        return 'Increment Memory by One'


class IncAbsolute(AbsoluteInstruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([IncrementMicroinstruction('DL')]))

    @property
    def name(self):
        return 'INC'

    @property
    def opcode(self):
        return 0xEE

    @property
    def description(self):
        return 'Increment Memory by One'


class IncAbsoluteX(AbsoluteXInstruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([IncrementMicroinstruction('DL')]))

    @property
    def name(self):
        return 'INC'

    @property
    def opcode(self):
        return 0xFE

    @property
    def description(self):
        return 'Increment Memory by One'
