from .addressing_mode import AddressingMode


class AbsoluteXAddressingMode(AddressingMode):
    def read_parameters(self, processor):
        address = processor.read16(processor.pc + 1) + processor.x
        page_crossed = self.pages_differ(address - processor.x, address)
        return address, page_crossed
