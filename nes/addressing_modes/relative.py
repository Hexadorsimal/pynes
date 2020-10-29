from .addressing_mode import AddressingMode


class RelativeAddressingMode(AddressingMode):
    def read_parameters(self, processor):
        offset = processor.read(processor.pc.value + 1)
        if offset < 0x80:
            address = processor.pc.value + 2 + offset
        else:
            address = processor.pc.value + 2 + offset - 0x100

        page_crossed = self.pages_differ(processor.pc.value, address)

        return address, page_crossed
