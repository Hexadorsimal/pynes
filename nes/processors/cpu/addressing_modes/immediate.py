from nes.processors.cpu import Cpu
from .parameter_reader import ParameterReader
from ..instructions import Instruction


class ImmediateParameterReader(ParameterReader):
    def read_parameter(self, cpu: Cpu, instruction: Instruction) -> int:
        return (instruction.params[0] << 8) | instruction.params[1]
