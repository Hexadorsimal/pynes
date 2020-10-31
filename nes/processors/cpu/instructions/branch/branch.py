from ..instruction import Instruction


class BranchInstruction(Instruction):
    def meets_branch_condition(self, processor):
        raise NotImplementedError

    def execute(self, processor):
        if self.meets_branch_condition(processor):
            page_before = processor.pc.hi

            processor.pc.value = self.read_source(processor)
            self.branch_taken = True

            page_after = processor.pc.hi
            self.page_crossed = page_before != page_after
        else:
            self.branch_taken = False
