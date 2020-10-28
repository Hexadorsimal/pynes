from nes.instructions import Instruction


class Stx(Instruction):
    def execute(self):
        x = self.get('x')

        return {
            'write': x,
        }
