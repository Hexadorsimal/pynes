from .bus_request import ReadRequest, WriteRequest


class BusDevice:
    def handle_bus_request(self, request):
        if isinstance(request, ReadRequest):
            return self.handle_read_request(request)
        elif isinstance(request, WriteRequest):
            return self.handle_write_request(request)

    def handle_read_request(self, request):
        raise NotImplementedError

    def handle_write_request(self, request):
        raise NotImplementedError
