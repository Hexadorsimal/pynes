from nes.cpu.cycle import Cycle
from nes.cpu.microinstructions import MoveMicroinstruction
from .absolute_instruction import AbsoluteInstruction
from .indirect_absolute_instruction import IndirectAbsoluteInstruction


class JmpAbsolute(AbsoluteInstruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([MoveMicroinstruction('ADL', 'PCL')]))
        self.cycles.append(Cycle([MoveMicroinstruction('ADH', 'PCH')]))

    @property
    def name(self):
        return 'JMP'

    @property
    def opcode(self):
        return 0x4C

    @property
    def description(self):
        return 'Jump to New Location'


class JmpIndirectAbsolute(IndirectAbsoluteInstruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([MoveMicroinstruction('ADL', 'PCL')]))
        self.cycles.append(Cycle([MoveMicroinstruction('ADH', 'PCH')]))

    @property
    def name(self):
        return 'JMP'

    @property
    def opcode(self):
        return 0x6C

    @property
    def description(self):
        return 'Jump to New Location'
