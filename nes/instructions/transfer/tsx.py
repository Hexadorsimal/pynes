from nes.instructions import Instruction


class Tsx(Instruction):
    def execute(self):
        s = self.get('s')

        return {
            'x': s,
        }
