from nes.instructions import Instruction


class Stx(Instruction):
    def execute(self, processor):
        x = processor.x
        addr = self.parameter

        processor.write(addr, x.value)
