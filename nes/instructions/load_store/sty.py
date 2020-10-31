from nes.instructions import Instruction


class Sty(Instruction):
    def execute(self, processor):
        self.write_result(processor, processor.y.value)
