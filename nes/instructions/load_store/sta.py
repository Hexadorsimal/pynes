from nes.instructions import Instruction


class Sta(Instruction):
    def execute(self, processor):
        a = processor.a
        addr = self.parameter

        processor.write(addr, a.value)
