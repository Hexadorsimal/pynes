from .addressing_modes import AddressingMode
from .addressing_modes.relative import RelativeAddressingMode


class Instruction:
    def __init__(self, addressing_mode: AddressingMode, cycles: int = 0, page_cycles: int = 0, parameter: int = 0):
        self.addressing_mode = addressing_mode
        self.base_cycles = cycles
        self.page_cycles = page_cycles

        self.parameter = parameter
        self.page_crossed = False
        self.branch_taken = False

    def __repr__(self):
        s = f'{self.__class__.__name__.upper()} ({self.addressing_mode})'
        if self.parameter is not None:
            s += f' {self.parameter:#X}'
        return s

    @property
    def size(self):
        return self.addressing_mode.instruction_size

    def read_source(self, processor):
        return self.addressing_mode.read_source(processor, self.parameter)

    def write_result(self, processor, value):
        self.addressing_mode.write_result(processor, self.parameter, value)

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
