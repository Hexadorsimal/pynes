from nes.instructions import Instruction


class Sei(Instruction):
    def execute(self, processor):
        processor.p.i.set()
