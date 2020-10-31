from nes.instructions import Instruction


class Sta(Instruction):
    def execute(self, processor):
        self.write_result(processor, processor.a.value)
