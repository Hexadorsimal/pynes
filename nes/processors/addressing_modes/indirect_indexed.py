from nes.processors.cpu import Cpu, Instruction, ParameterReader


class IndirectIndexedParameterReader(ParameterReader):
    def read_parameter(self, cpu: Cpu, instruction: Instruction) -> int:
        lo_addr = instruction.params[0]
        hi_addr = (lo_addr + 1) & 0x00ff
        lo = cpu.read(lo_addr)
        hi = cpu.read(hi_addr)
        addr = (hi << 8) | lo
        indexed_addr = (addr + cpu.y.read()) & 0xffff
        return cpu.read(indexed_addr)
