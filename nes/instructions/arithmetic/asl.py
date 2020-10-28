from ..instruction import Instruction


class Asl(Instruction):
    def execute(self):
        addr = self.addressing_mode.calculate_address()

        value = self.read(addr)
        c = (value >> 7) & 0x01
        value = value << 1

        self.write(addr, value)

        z = value == 0
        n = value & 0x80

        return {
            'z': z,
            'n': n,
            'c': c,
            'write': value,
        }
