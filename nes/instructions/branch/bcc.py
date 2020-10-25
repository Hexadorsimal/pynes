from nes.instructions import Instruction


class Bcc(Instruction):
    def execute(self):
        c = self.get('c')

        if not c:
            return {
                'pc': self.addressing_mode.calculate_address(),
                'branch_taken': True,
            }
        else:
            return {
                'branch_taken': False
            }
