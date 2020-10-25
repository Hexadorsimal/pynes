from nes.instructions import Instruction


class Jsr(Instruction):
    def execute(self):
        addr = self.addressing_mode.calculate_address()
        pc = self.get('pc')

        return {
            'push16': pc - 1,
            'pc': addr,
        }
