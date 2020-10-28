from nes.instructions import Instruction


class Txs(Instruction):
    def execute(self):
        x = self.get('x')

        return {
            's': x,
        }
