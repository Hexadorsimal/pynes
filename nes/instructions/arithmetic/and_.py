from ..instruction import Instruction


class And(Instruction):
    def execute(self):
        addr = self.addressing_mode.calculate_address()

        a = self.get('a') & self.read(addr)
        z = a == 0
        n = a & 0x80

        return {
            'a': a,
            'z': z,
            'n': n,
        }
