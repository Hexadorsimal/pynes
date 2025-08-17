class BusAttachment:
    def __init__(self, name: str):
        self.name = name

    def read(self, addr: int):
        raise NotImplementedError

    def write(self, addr: int, value: int):
        raise NotImplementedError
