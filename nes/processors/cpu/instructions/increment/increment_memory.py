from .increment import IncrementInstruction


class IncrementMemoryInstruction(IncrementInstruction):
    def increment(self, processor):
        value = self.read_source(processor)
        value += self.amount
        self.write_result(processor, value)
        return value
