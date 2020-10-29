from nes.addressing_modes import AddressingMode
from nes.addressing_modes.relative import RelativeAddressingMode


class Instruction:
    def __init__(self, addressing_mode: AddressingMode, size: int, cycles: int, page_cycles: int, parameter: int):
        self.addressing_mode = addressing_mode
        self.size = size
        self.base_cycles = cycles
        self.page_cycles = page_cycles

        self.parameter = parameter
        self.page_crossed = False
        self.branch_taken = False

    @property
    def cycles(self) -> int:
        total_cycles = self.base_cycles
        if isinstance(self.addressing_mode, RelativeAddressingMode) and self.branch_taken:
            total_cycles += 1

        if self.page_crossed:
            total_cycles += self.page_cycles

        return total_cycles

    def execute(self, processor):
        raise NotImplementedError
