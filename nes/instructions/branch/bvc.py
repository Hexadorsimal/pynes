from nes.instructions import Instruction


class Bvc(Instruction):
    def execute(self, processor):
        v = processor.p.v
        offset = self.parameter

        if not v:
            page_before = processor.pc.hi

            processor.pc.value += offset
            self.branch_taken = True

            page_after = processor.pc.hi
            self.page_crossed = page_before != page_after
        else:
            self.branch_taken = False
