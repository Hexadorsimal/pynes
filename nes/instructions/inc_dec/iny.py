from nes.instructions import Instruction


class Iny(Instruction):
    def execute(self, processor):
        processor.y.value += 1

        processor.p.z.update(processor.y.value)
        processor.p.n.update(processor.y.value)
