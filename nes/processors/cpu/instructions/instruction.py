from dataclasses import dataclass

from nes.processors.cpu.addressing_modes import RelativeAddressingMode
from .. import Cpu
from ..decoder import Opcode


@dataclass
class ExecutionResult:
    base_cycles: int
    total_cycles: int
    page_crossed: bool
    branch_taken: bool


@dataclass
class Instruction:
    opcode: Opcode
    data: bytes

    def execute(self, cpu: Cpu) -> ExecutionResult:
        raise NotImplementedError


def calculate_cycles(opcode: Opcode, result: ExecutionResult) -> int:
    total_cycles = opcode.base_cycles
    if isinstance(opcode.addressing_mode, RelativeAddressingMode) and result.branch_taken:
        total_cycles += 1

    if result.page_crossed:
        total_cycles += opcode.page_cycles

    return total_cycles
