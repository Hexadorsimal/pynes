from .addressing_mode import AddressingMode


class AbsoluteYAddressingMode(AddressingMode):
    def calculate_address(self, processor):
        address = processor.read16(processor.registers['pc'] + 1) + processor.registers['y']
        page_crossed = self.pages_differ(address - processor.registers['y'], address)
        return address, page_crossed
