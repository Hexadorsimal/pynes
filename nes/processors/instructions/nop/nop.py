from nes.processors.cpu.instruction import Instruction
from nes.processors.cpu import Cpu


class Nop(Instruction):
    def execute(self, cpu: Cpu) -> None:
        pass
