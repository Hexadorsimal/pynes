from nes.instructions import Instruction


class Sty(Instruction):
    def execute(self, processor):
        y = processor.y
        addr = self.parameter

        processor.write(addr, y.value)
