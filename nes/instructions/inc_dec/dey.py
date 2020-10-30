from nes.instructions import Instruction


class Dey(Instruction):
    def execute(self):
        y = self.get('y') - 1

        return {
            'y': y,
            'z': y == 0,
            'n': y & 0x80 != 0,
        }
