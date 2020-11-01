class BusDevice:
    def read(self, addr):
        raise NotImplementedError

    def write(self, addr, value):
        raise NotImplementedError
