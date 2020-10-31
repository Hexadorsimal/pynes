from .addressing_mode import AddressingMode


class AccumulatorAddressingMode(AddressingMode):
    @property
    def instruction_size(self):
        return 1

    def read_source(self, processor):
        return processor.a.value

    def write_result(self, processor, value):
        processor.a.value = value
