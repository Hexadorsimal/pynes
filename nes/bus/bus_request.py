class BusRequest:
    def __init__(self, bus_name):
        self.bus_name = bus_name


class ReadRequest(BusRequest):
    def __init__(self, bus_name, addr):
        super().__init__(bus_name)
        self.addr = addr


class WriteRequest(BusRequest):
    def __init__(self, bus_name, addr, data):
        super().__init__(bus_name)
        self.addr = addr
        self.data = data
