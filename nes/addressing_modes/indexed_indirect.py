from .addressing_mode import AddressingMode


class IndexedIndirectAddressingMode(AddressingMode):
    @property
    def instruction_size(self):
        return 2

    def calculate_address(self, processor, parameter):
        lo_addr = (parameter + processor.x.value) & 0x00ff
        hi_addr = (lo_addr + 1) & 0x00ff
        lo = processor.read(lo_addr)
        hi = processor.read(hi_addr)
        return (hi << 8) | lo
