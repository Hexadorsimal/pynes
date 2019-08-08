import logging


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
