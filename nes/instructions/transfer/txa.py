from nes.instructions import Instruction


class Txa(Instruction):
    def execute(self):
        x = self.get('x')

        return {
            'a': x,
            'z': x == 0,
            'n': x & 0x80,
        }
