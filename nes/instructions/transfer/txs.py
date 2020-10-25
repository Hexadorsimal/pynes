from nes.instructions import Instruction


class Tsx(Instruction):
    def execute(self):
        x = self.get('x')

        return {
            's': x,
        }
