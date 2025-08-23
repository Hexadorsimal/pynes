from nes.processors.cpu import Cpu, Instruction, ParameterReader


class AbsoluteYParameterReader(ParameterReader):
    def read_parameter(self, cpu: Cpu, instruction: Instruction) -> int:
        addr = (instruction.params[0] << 8) | instruction.params[0]
        addr += cpu.y.read()
        return cpu.read(addr)
