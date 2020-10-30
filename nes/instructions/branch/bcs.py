from nes.instructions import Instruction


class Bcs(Instruction):
    def execute(self, processor):
        c = processor.p.c
        offset = self.parameter

        if c:
            page_before = processor.pc.hi

            processor.pc.value += offset
            self.branch_taken = True

            page_after = processor.pc.hi
            self.page_crossed = page_before != page_after
        else:
            self.branch_taken = False
