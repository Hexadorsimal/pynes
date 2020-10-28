from ..instruction import Instruction


class Ora(Instruction):
    def execute(self):
        addr = self.addressing_mode.calculate_address()
        value = self.read(addr)

        a = self.get('a')
        a |= value

        return {
            'a': a,
            'z': a == 0,
            'n': a & 0x80 != 0,
        }
