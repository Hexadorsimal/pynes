from nes.instructions import Instruction


class Pha(Instruction):
    def execute(self):
        a = self.get('a')

        return {
            'push': a,
        }
