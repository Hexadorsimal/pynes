from nes.processors.cpu import Cpu
from nes.processors.cpu.instructions import Instruction


class ParameterReader:
    def read_parameter(self, cpu: Cpu, instruction: Instruction) -> int:
        raise NotImplementedError

