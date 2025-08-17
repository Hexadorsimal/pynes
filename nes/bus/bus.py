import logging
from dataclasses import dataclass

from .address_range import AddressRange
from .bus_device import BusDevice


@dataclass
class DeviceEntry:
    device: BusDevice
    addr_range: AddressRange


class Bus(BusDevice):
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.devices: dict[str, DeviceEntry] = {}

    def attach_device(self, name: str, device: BusDevice, addr: int, size: int) -> None:
        self.devices[name] = DeviceEntry(device, AddressRange(addr, size))

    def detach_device(self, device_name: str):
        self.devices.pop(device_name)

    def find_device_entry(self, addr: int) -> DeviceEntry | None:
        for entry in self.devices.values():
            if addr in entry.addr_range:
                return entry

        return None

    def read(self, addr: int) -> int:
        entry = self.find_device_entry(addr)
        if entry:
            return entry.device.read(addr - entry.addr_range.start)
        else:
            raise RuntimeError('Unhandled memory read request')

    def write(self, addr: int, value: int) -> None:
        entry = self.find_device_entry(addr)
        if entry:
            entry.device.write(addr - entry.addr_range.start, value)
        else:
            raise RuntimeError('Unhandled memory write request')
