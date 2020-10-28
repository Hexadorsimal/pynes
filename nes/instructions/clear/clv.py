from nes.instructions import Instruction


class Clv(Instruction):
    def execute(self):
        return {
            'v': False
        }
