from nes.instructions import Instruction


class Tsx(Instruction):
    def execute(self, processor):
        processor.x.value = processor.s.value
