from nes.instructions import Instruction


class Sta(Instruction):
    def execute(self):
        a = self.get('a')

        return {
            'write': a,
        }
