from nes.instructions import Instruction


class Clv(Instruction):
    def execute(self, processor):
        processor.p.v.clear()
