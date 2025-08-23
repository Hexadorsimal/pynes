from nes.processors.cpu import Cpu, ParameterReader, Instruction


class AbsoluteParameterReader(ParameterReader):
    def read_parameter(self, cpu: Cpu, instruction: Instruction) -> int:
        addr = (instruction.params[0] << 8) | instruction.params[0]
        return cpu.read(addr)
