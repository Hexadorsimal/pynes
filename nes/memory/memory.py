class Memory:
    def __init__(self, size):
        self.size = size

    def read(self, addr):
        raise NotImplementedError

    def write(self, addr, data):
        raise NotImplementedError
