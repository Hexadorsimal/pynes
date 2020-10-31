from .addressing_mode import AddressingMode


class IndirectIndexedAddressingMode(AddressingMode):
    @property
    def instruction_size(self):
        return 2

    def calculate_address(self, processor, parameter):
        lo_addr = parameter
        hi_addr = (lo_addr + 1) & 0x00ff
        lo = processor.read(lo_addr)
        hi = processor.read(hi_addr)
        addr = (hi << 8) | lo
        return (addr + processor.y.value) & 0xffff
