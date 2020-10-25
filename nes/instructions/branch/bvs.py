from nes.instructions import Instruction


class Bvs(Instruction):
    def execute(self):
        v = self.get('v')

        if v:
            return {
                'pc': self.addressing_mode.calculate_address(),
                'branch_taken': True,
            }
        else:
            return {
                'branch_taken': False,
            }
