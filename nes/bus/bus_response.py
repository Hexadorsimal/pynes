class BusResponse:
    def __init__(self, request, device):
        self.request = request
        self.device = device


class ReadResponse(BusResponse):
    def __init__(self, request, device, data):
        super().__init__(request, device)
        self.data = data


class WriteResponse(BusResponse):
    pass
