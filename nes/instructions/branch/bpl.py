from nes.instructions import Instruction


class Bpl(Instruction):
    def execute(self, processor):
        n = processor.p.n
        offset = self.parameter

        if not n:
            page_before = processor.pc.hi

            processor.pc.value += offset
            self.branch_taken = True

            page_after = processor.pc.hi
            self.page_crossed = page_before != page_after
        else:
            self.branch_taken = False
