class AddressingMode:
    def __repr__(self):
        return self.__class__.__name__.replace('AddressingMode', '')

    @property
    def instruction_size(self):
        raise NotImplementedError

    @property
    def parameter_size(self):
        return self.instruction_size - 1

    def calculate_address(self, processor, parameter):
        raise NotImplementedError

    def read_source(self, processor, parameter):
        addr = self.calculate_address(processor, parameter)
        return processor.read(addr)

    def write_result(self, processor, parameter, value):
        addr = self.calculate_address(processor, parameter)
        processor.write(addr, value)

    @staticmethod
    def pages_differ(a, b):
        return a & 0xFF00 != b & 0xFF00
