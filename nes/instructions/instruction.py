from nes.addressing_modes.relative import RelativeAddressingMode
from nes.registers import Register


class Instruction:
    def __init__(self, processor, addressing_mode, size, cycles, page_cycles):
        self.processor = processor
        self.addressing_mode = addressing_mode
        self.size = size
        self.base_cycles = cycles
        self.page_cycles = page_cycles

        self.page_crossed = False
        self.branch_taken = False

    def get(self, item):
        if item in self.processor.registers:
            return self.processor.registers[item].get()
        elif item in self.processor.flags:
            return self.processor.flags[item].get()
        else:
            raise ValueError(f'{item} not found in processor')

    def read(self, addr):
        if isinstance(addr, Register):
            return addr.get()
        else:
            return self.processor.bus.read(addr)

    def write(self, addr, value):
        if isinstance(addr, Register):
            addr.set(value)
        else:
            self.processor.bus.write(addr, value)

    @property
    def cycles(self):
        total_cycles = self.base_cycles
        if isinstance(self.addressing_mode, RelativeAddressingMode) and self.branch_taken:
            total_cycles += 1

        if self.page_crossed:
            total_cycles += self.page_cycles

        return total_cycles

    def execute(self):
        raise NotImplementedError
