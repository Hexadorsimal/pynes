from nes.instructions import Instruction


class Tay(Instruction):
    def execute(self, processor):
        value = processor.a.value

        processor.y.value = value
        processor.p.n.update(value)
        processor.p.z.update(value)
