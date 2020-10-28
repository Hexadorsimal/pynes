from nes.instructions import Instruction


class Bmi(Instruction):
    def execute(self):
        n = self.get('n')

        if n:
            return {
                'pc': self.addressing_mode.calculate_address(),
                'branch_taken': True,
            }
        else:
            return {
                'branch_taken': False
            }