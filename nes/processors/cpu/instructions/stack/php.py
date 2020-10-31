from ..instruction import Instruction


class Php(Instruction):
    def execute(self, processor):
        processor.push(processor.p.value)
