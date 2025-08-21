from nes.processors.cpu import Cpu
from .parameter_reader import ParameterReader
from ..instructions import Instruction


class IndexedIndirectParameterReader(ParameterReader):
    def read_parameter(self, cpu: Cpu, instruction: Instruction) -> int:
        lo_addr = (instruction.params[0] + cpu.x.read()) & 0x00ff
        hi_addr = (lo_addr + 1) & 0x00ff
        lo = cpu.read(lo_addr)
        hi = cpu.read(hi_addr)
        return (hi << 8) | lo
