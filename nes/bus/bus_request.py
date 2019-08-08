class BusRequest:
    def __init__(self, bus):
        self.bus = bus


class ReadRequest(BusRequest):
    def __init__(self, bus, addr):
        super().__init__(bus)
        self.addr = addr


class WriteRequest(BusRequest):
    def __init__(self, bus, addr, data):
        super().__init__(bus)
        self.addr = addr
        self.data = data
