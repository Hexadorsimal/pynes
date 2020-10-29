class AddressingMode:
    def read_parameter(self, processor):
        raise NotImplementedError

    @staticmethod
    def pages_differ(a, b):
        return a & 0xFF00 != b & 0xFF00
