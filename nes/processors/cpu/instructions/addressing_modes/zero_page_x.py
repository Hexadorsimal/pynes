from .addressing_mode import AddressingMode
from .parameter_reader import ParameterReader
from .. import Instruction
from ... import Cpu


class ZeroPageXAddressingMode(AddressingMode):
    @property
    def instruction_size(self) -> int:
        return 2

    def calculate_address(self, cpu: Cpu, parameter: int) -> int:
        return (parameter + cpu.x.value) & 0x00ff


class ZeroPageParameterReader(ParameterReader):
    def read_parameter(self, cpu: Cpu, instruction: Instruction) -> int:
        return cpu.read(instruction.parameter + cpu.x.value)
