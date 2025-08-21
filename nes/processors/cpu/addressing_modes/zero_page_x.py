from .parameter_reader import ParameterReader
from nes.processors.cpu.instructions import Instruction
from nes.processors.cpu import Cpu


class ZeroPageXParameterReader(ParameterReader):
    def read_parameter(self, cpu: Cpu, instruction: Instruction) -> int:
        addr = (instruction.parameter + cpu.x.value) & 0x00ff
        return cpu.read(addr)
