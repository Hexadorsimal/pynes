from ..instruction import Instruction


class Pla(Instruction):
    def execute(self, processor):
        value = processor.pull()

        processor.a.value = value
        processor.p.z.update(value)
        processor.p.n.update(value)
