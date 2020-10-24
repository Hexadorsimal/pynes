import logging
from .address_range import AddressRange


class Bus:
    def __init__(self, name):
        self.name = name
        self.logger = logging.getLogger(__name__)
        self.devices = {}

    def attach_device(self, device, addr, size):
        self.devices[device.name] = {
            'device': device,
            'addr_range': AddressRange(addr, size),
        }

    def remove_device(self, device):
        self.devices.pop(device.name)

    def find_device(self, addr):
        for entry in self.devices.values():
            if addr in entry['addr_range']:
                return entry['device']

    def read(self, addr):
        device = self.find_device(addr)
        if device:
            return device.read(addr)
        else:
            raise RuntimeError('Unhandled memory read request')

    def write(self, addr, value):
        device = self.find_device(addr)
        if device:
            device.write(addr, value)
        else:
            raise RuntimeError('Unhandled memory write request')
