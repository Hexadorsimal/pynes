from nes.instructions import Instruction


class Dex(Instruction):
    def execute(self, processor):
        processor.x.value -= 1

        processor.p.z.update(processor.x.value)
        processor.p.n.update(processor.x.value)
