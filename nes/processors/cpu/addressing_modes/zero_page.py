from .parameter_reader import ParameterReader
from nes.processors.cpu.instructions import Instruction
from nes.processors.cpu import Cpu


class ZeroPageParameterReader(ParameterReader):
    def read_parameter(self, cpu: Cpu, instruction: Instruction) -> int:
        return cpu.read(instruction.params[0])
