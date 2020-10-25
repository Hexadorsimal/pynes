from ..instruction import Instruction


class Cmp(Instruction):
    def execute(self):
        a = self.get('a')

        addr = self.addressing_mode.calculate_address()
        b = self.read(addr)

        c = a - b

        return {
            'z': c == 0,
            'n': c & 0x80 != 0,
            'c': a >= b,
        }
