from nes.instructions import Instruction


class Bne(Instruction):
    def execute(self, processor):
        z = processor.p.z
        offset = self.parameter

        if not z:
            page_before = processor.pc.hi

            processor.pc.value += offset
            self.branch_taken = True

            page_after = processor.pc.hi
            self.page_crossed = page_before != page_after
        else:
            self.branch_taken = False
