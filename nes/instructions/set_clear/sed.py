from nes.instructions import Instruction


class Sed(Instruction):
    def execute(self, processor):
        processor.p.d.set()
