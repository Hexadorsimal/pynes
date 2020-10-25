from ..instruction import Instruction


class Sbc(Instruction):
    def execute(self):
        addr = self.addressing_mode.calculate_address()
        a0 = self.get('a')
        b0 = self.read(addr)
        c0 = self.get('c')

        a = a0 - b0 - (1 - c0)
        z = a == 0
        n = a & 0x80 != 0
        c = a > 0

        if (a0 ^ b0) & 0x80 != 0 and (a0 ^ a) & 0x80 != 0:
            v = True
        else:
            v = False

        return {
            'a': a,
            'z': z,
            'n': n,
            'c': c,
            'v': v
        }
