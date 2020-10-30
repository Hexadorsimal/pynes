from nes.instructions import Instruction


class Jmp(Instruction):
    def execute(self, processor):
        processor.pc.value = self.parameter
