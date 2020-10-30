class AddressingMode:
    def __repr__(self):
        return self.__class__.__name__.replace('AddressingMode', '')

    def read_parameter(self, processor):
        raise NotImplementedError

    @staticmethod
    def pages_differ(a, b):
        return a & 0xFF00 != b & 0xFF00
