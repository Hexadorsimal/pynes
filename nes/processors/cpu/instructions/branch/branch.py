from ..instruction import Instruction
from ... import Cpu


class BranchInstruction(Instruction):
    def meets_branch_condition(self, cpu: Cpu) -> bool:
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


class Bcc(BranchInstruction):
    def meets_branch_condition(self, cpu: Cpu) -> bool:
        return not cpu.p.c


class Bcs(BranchInstruction):
    def meets_branch_condition(self, cpu: Cpu) -> bool:
        return cpu.p.c


class Bne(BranchInstruction):
    def meets_branch_condition(self, cpu: Cpu) -> bool:
        return not cpu.p.z


class Beq(BranchInstruction):
    def meets_branch_condition(self, cpu: Cpu) -> bool:
        return cpu.p.z


class Bpl(BranchInstruction):
    def meets_branch_condition(self, cpu: Cpu) -> bool:
        return not cpu.p.n


class Bmi(BranchInstruction):
    def meets_branch_condition(self, cpu: Cpu) -> bool:
        return cpu.p.n


class Bvc(BranchInstruction):
    def meets_branch_condition(self, cpu: Cpu) -> bool:
        return not cpu.p.v


class Bvs(BranchInstruction):
    def meets_branch_condition(self, cpu: Cpu) -> bool:
        return cpu.p.v
