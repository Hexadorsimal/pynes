from nes.processors.cpu import Cpu, Instruction, ParameterReader


class ZeroPageXParameterReader(ParameterReader):
    def read_parameter(self, cpu: Cpu, instruction: Instruction) -> int:
        addr = (instruction.params[0] + cpu.x.value) & 0x00ff
        return cpu.read(addr)
