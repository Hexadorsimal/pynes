from nes.instructions import Instruction


class Sta(Instruction):
    def execute(self):
        x = self.get('x')

        return {
            'write': x,
        }
