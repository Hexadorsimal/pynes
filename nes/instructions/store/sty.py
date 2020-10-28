from nes.instructions import Instruction


class Sty(Instruction):
    def execute(self):
        y = self.get('y')

        return {
            'write': y,
        }
