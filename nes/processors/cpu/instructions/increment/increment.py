from ..instruction import Instruction


class IncrementInstruction(Instruction):
    amount = 1

    def execute(self, processor):
        value = self.increment(processor)
        self.update_flags(processor, value)

    def increment(self, processor):
        raise NotImplementedError

    @staticmethod
    def update_flags(processor, value):
        processor.p.z.update(value)
        processor.p.n.update(value)
