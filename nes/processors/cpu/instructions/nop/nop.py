from ..instruction import Instruction
from ... import Cpu


class Nop(Instruction):
    def execute(self, cpu: Cpu) -> None:
        pass
