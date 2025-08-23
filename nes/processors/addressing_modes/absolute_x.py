from nes.processors.cpu import Cpu, Instruction, ParameterReader


class AbsoluteXParameterReader(ParameterReader):
    def read_parameter(self, cpu: Cpu, instruction: Instruction) -> int:
        addr = (instruction.params[0] << 8) | instruction.params[0]
        addr += cpu.x.read()
        return cpu.read(addr)
