from nes.processors.cpu import Cpu, Instruction, ParameterReader


class ZeroPageParameterReader(ParameterReader):
    def read_parameter(self, cpu: Cpu, instruction: Instruction) -> int:
        addr = instruction.params[0]
        return cpu.read(addr)
