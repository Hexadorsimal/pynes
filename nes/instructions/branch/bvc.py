from nes.instructions import Instruction


class Bvc(Instruction):
    def execute(self):
        v = self.get('v')

        if not v:
            return {
                'pc': self.addressing_mode.calculate_address(),
                'branch_taken': True,
            }
        else:
            return {
                'branch_taken': False,
            }
