from nes.instructions import Instruction


class Php(Instruction):
    def execute(self):
        p = self.get('p')

        return {
            'push': p,
        }
