from nes.instructions import Instruction


class BranchInstruction(Instruction):
    def meets_branch_condition(self, processor):
        raise NotImplementedError

    def execute(self, processor):
        offset = self.read_source(processor)

        if self.meets_branch_condition(processor):
            page_before = processor.pc.hi

            processor.pc.value += offset
            self.branch_taken = True

            page_after = processor.pc.hi
            self.page_crossed = page_before != page_after
        else:
            self.branch_taken = False
