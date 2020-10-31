from nes.instructions import Instruction


class Plp(Instruction):
    def execute(self, processor):
        processor.p.value = processor.pull()
