from ..instruction import Instruction


class Sec(Instruction):
    def execute(self, processor):
        processor.p.c.set()
