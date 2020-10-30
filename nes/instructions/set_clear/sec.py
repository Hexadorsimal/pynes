from nes.instructions import Instruction


class Sec(Instruction):
    def execute(self, processor):
        processor.p.c.set()
