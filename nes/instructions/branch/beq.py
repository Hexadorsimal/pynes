from nes.instructions import Instruction


class Beq(Instruction):
    def execute(self, processor):
        z = processor.p.z
        offset = self.read_source(processor)

        if z:
            page_before = processor.pc.hi

            processor.pc.value += offset
            self.branch_taken = True

            page_after = processor.pc.hi
            self.page_crossed = page_before != page_after
        else:
            self.branch_taken = False
