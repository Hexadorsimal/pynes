from .addressing_mode import AddressingMode
from .parameter_reader import ParameterReader
from nes.processors.cpu.instructions import Instruction
from nes.processors.cpu import Cpu


class ZeroPageAddressingMode(AddressingMode):
    @property
    def instruction_size(self) -> int:
        return 2


class ZeroPageParameterReader(ParameterReader):
    def read_parameter(self, cpu: Cpu, instruction: Instruction) -> int:
        return cpu.read(instruction.parameter)
