from nes.processors.cpu import Cpu, Instruction, ParameterReader


class RelativeParameterReader(ParameterReader):
    def read_parameter(self, cpu: Cpu, instruction: Instruction) -> int:
        return instruction.params[0]
