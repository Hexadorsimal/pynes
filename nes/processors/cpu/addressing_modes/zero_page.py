from .parameter_reader import ParameterReader
from nes.processors.cpu.instructions import Instruction
from nes.processors.cpu import Cpu


class ZeroPageParameterReader(ParameterReader):
    def read_parameter(self, cpu: Cpu, instruction: Instruction) -> int:
        addr = instruction.params[0]
        return cpu.read(addr)
