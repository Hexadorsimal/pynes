from ..instruction import Instruction


class Inx(Instruction):
    def execute(self, processor):
        processor.x.value += 1

        processor.p.z.update(processor.x.value)
        processor.p.n.update(processor.x.value)
