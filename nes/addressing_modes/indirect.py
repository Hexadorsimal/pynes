from .addressing_mode import AddressingMode


class IndirectAddressingMode(AddressingMode):
    @property
    def instruction_size(self):
        return 3

    def calculate_address(self, processor, parameter):
        lo_addr = parameter
        hi_addr = (lo_addr + 1) & 0xffff
        lo = processor.read(lo_addr)
        hi = processor.read(hi_addr)
        return (hi << 8) | lo

    def read_source(self, processor, parameter):
        raise RuntimeError('This should never be called')

    def write_result(self, processor, parameter, value):
        raise RuntimeError('This should never be called')
