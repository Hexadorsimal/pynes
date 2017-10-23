from nes.cpu.cycle import Cycle
from nes.cpu.operations import MoveOperation
from .absolute_instruction import AbsoluteInstruction
from .indirect_absolute_instruction import IndirectAbsoluteInstruction


class JmpAbsolute(AbsoluteInstruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([MoveOperation('ADL', 'PCL')]))
        self.cycles.append(Cycle([MoveOperation('ADH', 'PCH')]))

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
        self.cycles.append(Cycle([MoveOperation('ADL', 'PCL')]))
        self.cycles.append(Cycle([MoveOperation('ADH', 'PCH')]))

    @property
    def name(self):
        return 'JMP'

    @property
    def opcode(self):
        return 0x6C

    @property
    def description(self):
        return 'Jump to New Location'
