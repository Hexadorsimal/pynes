from nes.instructions import Instruction


class Bne(Instruction):
    def execute(self):
        z = self.get('z')

        if z:
            return {
                'pc': self.addressing_mode.calculate_address(),
                'branch_taken': True,
            }
        else:
            return {
                'branch_taken': False
            }
