class BusDevice:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name

    def read(self, addr):
        raise NotImplementedError

    def write(self, addr, value):
        raise NotImplementedError
