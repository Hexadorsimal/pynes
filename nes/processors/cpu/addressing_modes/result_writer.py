from nes.processors.cpu import Cpu
from nes.processors.cpu.instructions import Instruction


class ResultWriter:
    def write_result(self, cpu: Cpu, instruction: Instruction, value: int) -> None:
        raise NotImplementedError
