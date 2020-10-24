class BusDevice:
    @property
    def name(self):
        raise NotImplementedError

    def read(self, addr):
        raise NotImplementedError

    def write(self, addr, value):
        raise NotImplementedError
