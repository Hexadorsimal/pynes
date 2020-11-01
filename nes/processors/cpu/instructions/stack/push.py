from ..instruction import Instruction


class PushInstruction(Instruction):
    src_reg = None

    def execute(self, processor):
        processor.push(processor.registers[self.src_reg].value)
