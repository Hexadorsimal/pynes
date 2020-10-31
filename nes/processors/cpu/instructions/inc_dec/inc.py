from ..instruction import Instruction


class Inc(Instruction):
    def execute(self, processor):
        value = self.read_source(processor)

        value += 1

        processor.p.z.update(value)
        processor.p.n.update(value)

        self.write_result(processor, value)
