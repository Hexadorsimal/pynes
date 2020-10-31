from ..instruction import Instruction


class Cli(Instruction):
    def execute(self, processor):
        processor.p.i.clear()
