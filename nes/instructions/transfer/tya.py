from nes.instructions import Instruction


class Tya(Instruction):
    def execute(self):
        y = self.get('y')

        return {
            'a': y,
            'z': y == 0,
            'n': y & 0x80,
        }
