import logging
from .bus_request import ReadRequest, WriteRequest
from .bus_response import ReadResponse, WriteResponse


class Bus:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.devices = []

    def add_device(self, device):
        self.devices.append(device)

    def remove_device(self, device):
        self.devices.remove(device)

    def send_request(self, request):
        for device in self.devices:
            response = device.handle_request(request)
            if response:
                return response

    def read(self, addr):
        response = self.send_request(ReadRequest('cpu', addr))
        if response:
            return response.data
        else:
            raise RuntimeError('Unhandled memory read request')

    def write(self, addr, data):
        response = self.send_request(WriteRequest('cpu', addr, data))
        if not response:
            raise RuntimeError('Unhandled memory write request')
