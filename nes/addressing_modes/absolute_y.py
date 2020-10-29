from .addressing_mode import AddressingMode


class AbsoluteYAddressingMode(AddressingMode):
    def read_parameters(self, processor):
        address = processor.read16(processor.pc.value + 1) + processor.y.value
        page_crossed = self.pages_differ(address - processor.y.value, address)
        return address, page_crossed
