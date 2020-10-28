from nes.instructions import Instruction


class Jmp(Instruction):
    def execute(self):
        addr = self.addressing_mode.calculate_address()

        return {
            'pc': addr,
        }
