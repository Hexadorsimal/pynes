class BusDevice:
    def read(self, addr: int):
        raise NotImplementedError

    def write(self, addr: int, value: int):
        raise NotImplementedError
