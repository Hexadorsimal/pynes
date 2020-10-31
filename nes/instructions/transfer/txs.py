from nes.instructions import Instruction


class Txs(Instruction):
    def execute(self, processor):
        processor.s.value = processor.x.value
