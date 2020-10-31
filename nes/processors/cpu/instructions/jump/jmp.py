from ..instruction import Instruction


class Jmp(Instruction):
    def execute(self, processor):
        processor.pc.value = self.addressing_mode.calculate_address(processor, self.parameter)
