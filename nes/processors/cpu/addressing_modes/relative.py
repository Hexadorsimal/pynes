from .parameter_reader import ParameterReader
from nes.processors.cpu.instructions import Instruction
from nes.processors.cpu import Cpu


class RelativeParameterReader(ParameterReader):
    def read_parameter(self, cpu: Cpu, instruction: Instruction) -> int:
        raise instruction.params[0]
