from nes.processors.cpu import Cpu
from .parameter_reader import ParameterReader
from ..instructions import Instruction


class IndirectParameterReader(ParameterReader):
    def read_parameter(self, cpu: Cpu, instruction: Instruction) -> int:
        lo_addr = instruction.params[0]
        hi_addr = (lo_addr + 1) & 0xffff
        lo = cpu.read(lo_addr)
        hi = cpu.read(hi_addr)
        addr = (hi << 8) | lo
        return cpu.read(addr)
