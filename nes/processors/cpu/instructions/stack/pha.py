from ..instruction import Instruction


class Pha(Instruction):
    def execute(self, processor):
        processor.push(processor.a.value)
