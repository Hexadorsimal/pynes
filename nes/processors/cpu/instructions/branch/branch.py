from ..instruction import Instruction
from ... import Cpu


class BranchInstruction(Instruction):
    def meets_branch_condition(self, cpu: Cpu):
        raise NotImplementedError

    def execute(self, cpu: Cpu) -> None:
        if self.meets_branch_condition(cpu):
            page_before = cpu.pc.hi

            cpu.pc.value = self.read_source(cpu)
            self.branch_taken = True

            page_after = cpu.pc.hi
            self.page_crossed = page_before != page_after
        else:
            self.branch_taken = False
