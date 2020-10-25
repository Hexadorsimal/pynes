from .addressing_mode import AddressingMode


class IndirectIndexedAddressingMode(AddressingMode):
    def calculate_address(self, processor):
        return processor.read16_bug(processor.bus.read(processor.registers['pc'] + 1)) + processor.registers['y']
