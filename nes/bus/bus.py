import logging
from .address_range import AddressRange
from .bus_device import BusDevice


class Bus(BusDevice):
    def __init__(self, name):
        super().__init__(name)
        self.logger = logging.getLogger(__name__)
        self.devices = {}

    def attach_device(self, device, addr, size):
        self.devices[device.name] = {
            'device': device,
            'addr_range': AddressRange(addr, size),
        }

    def detach_device(self, device):
        self.devices.pop(device.name)

    def find_device_entry(self, addr):
        for entry in self.devices.values():
            if addr in entry['addr_range']:
                return entry

    def read(self, addr):
        entry = self.find_device_entry(addr)
        if entry:
            return entry['device'].read(addr - entry['addr_range'].start)
        else:
            raise RuntimeError('Unhandled memory read request')

    def write(self, addr, value):
        entry = self.find_device_entry(addr)
        if entry:
            entry['device'].write(addr - entry['addr_range'].start, value)
        else:
            raise RuntimeError('Unhandled memory write request')
