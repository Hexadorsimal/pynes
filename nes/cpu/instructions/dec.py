from nes.cpu.cycle import Cycle
from nes.cpu.microinstructions import DecrementMicroinstruction
from .zeropage_instruction import ZeroPageInstruction
from .zeropagex_instruction import ZeroPageXInstruction
from .absolute_instruction import AbsoluteInstruction
from .absolutex_instruction import AbsoluteXInstruction


class DecZeroPage(ZeroPageInstruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([DecrementMicroinstruction('DL')]))

    @property
    def name(self):
        return 'DEC'

    @property
    def opcode(self):
        return 0xC6

    @property
    def description(self):
        return 'Decrement Memory by One'


class DecZeroPageX(ZeroPageXInstruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([DecrementMicroinstruction('DL')]))

    @property
    def name(self):
        return 'DEC'

    @property
    def opcode(self):
        return 0xD6

    @property
    def description(self):
        return 'Decrement Memory by One'


class DecAbsolute(AbsoluteInstruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([DecrementMicroinstruction('DL')]))

    @property
    def name(self):
        return 'DEC'

    @property
    def opcode(self):
        return 0xCE

    @property
    def description(self):
        return 'Decrement Memory by One'


class DecAbsoluteX(AbsoluteXInstruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([DecrementMicroinstruction('DL')]))

    @property
    def name(self):
        return 'DEC'

    @property
    def opcode(self):
        return 0xDE

    @property
    def description(self):
        return 'Decrement Memory by One'
