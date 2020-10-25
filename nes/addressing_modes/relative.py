from .addressing_mode import AddressingMode


class RelativeAddressingMode(AddressingMode):
    def calculate_address(self, processor):
        offset = processor.bus.read(processor.registers['pc'] + 1)
        if offset < 0x80:
            address = processor.registers['pc'] + 2 + offset
        else:
            address = processor.registers['pc'] + 2 + offset - 0x100

        page_crossed = self.pages_differ(processor.registers['pc'], address)

        return address, page_crossed
