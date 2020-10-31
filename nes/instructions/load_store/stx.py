from nes.instructions import Instruction


class Stx(Instruction):
    def execute(self, processor):
        self.write_result(processor, processor.x.value)
