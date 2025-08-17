import logging
from typing import Optional

from .address_range import AddressRange
from .bus_device import BusDevice


class Bus(BusDevice):
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.devices = {}

    def attach_device(self, name: str, device: BusDevice, addr: int, size: int) -> None:
        self.devices[name] = {
            'device': device,
            'addr_range': AddressRange(addr, size),
        }

    def detach_device(self, device_name: str):
        self.devices.pop(device_name)

    def find_device_at_addr(self, addr: int) -> BusDevice | None:
        for entry in self.devices.values():
            if addr in entry['addr_range']:
                return entry

        return None

    def read(self, addr: int) -> int:
        entry = self.find_device_at_addr(addr)
        if entry:
            return entry['device'].read(addr - entry['addr_range'].start)
        else:
            raise RuntimeError('Unhandled memory read request')

    def write(self, addr: int, value: int) -> None:
        entry = self.find_device_at_addr(addr)
        if entry:
            entry['device'].write(addr - entry['addr_range'].start, value)
        else:
            raise RuntimeError('Unhandled memory write request')
