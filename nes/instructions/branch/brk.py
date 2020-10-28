from nes.instructions import Instruction


class Brk(Instruction):
    def execute(self):
        pc = self.get('pc')
        p = self.get('p')

        self.processor.push16(pc)
        self.processor.push(p)

        pc = self.processor.read16(0xfffe)

        return {
            'pc': pc,
            'i': True,
        }