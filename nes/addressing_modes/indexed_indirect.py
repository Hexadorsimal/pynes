from .addressing_mode import AddressingMode


class IndexedIndirectAddressingMode(AddressingMode):
    def read_parameters(self, processor):
        return processor.read16_bug(processor.read(processor.pc.value + 1) + processor.x.value)
