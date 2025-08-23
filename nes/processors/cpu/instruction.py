from dataclasses import dataclass

from .parameter_reader import ParameterReader
from .result_writer import ResultWriter
from .decoder import Opcode


@dataclass
class ExecutionResult:
    base_cycles: int
    total_cycles: int
    page_crossed: bool
    branch_taken: bool


@dataclass
class Instruction:
    opcode: Opcode
    params: list[int]
    reader: ParameterReader | None = None
    writer: ResultWriter | None = None

    def execute(self, cpu) -> ExecutionResult:
        raise NotImplementedError


def calculate_cycles(opcode: Opcode, result: ExecutionResult) -> int:
    total_cycles = opcode.base_cycles
    branch_instructions = ['BCC', 'BCS', 'BNE', 'BEQ', 'BPL', 'BMI', 'BVC', 'BVS']

    if opcode.name in branch_instructions and result.branch_taken:
        total_cycles += 1

    if result.page_crossed:
        total_cycles += opcode.page_cycles

    return total_cycles


def pages_differ(a, b):
    return a & 0xFF00 != b & 0xFF00
