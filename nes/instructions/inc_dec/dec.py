from nes.instructions import Instruction


class Dec(Instruction):
    def execute(self, processor):
        addr = self.parameter
        value = processor.read(addr)

        value -= 1

        processor.p.z.update(value)
        processor.p.n.update(value)

        processor.write(addr, value)
