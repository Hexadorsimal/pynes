from .addressing_mode import AddressingMode


class AbsoluteXAddressingMode(AddressingMode):
    def calculate_address(self, processor):
        address = processor.read16(processor.registers['pc'] + 1) + processor.registers['x']
        page_crossed = self.pages_differ(address - processor.registers['x'], address)
        return address, page_crossed
