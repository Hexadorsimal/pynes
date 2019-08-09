from nes.bus import BusDevice, ReadRequest, WriteRequest
from .system_palette import SystemPalette
from .palette_ram import PaletteRam
from .name_table_ram import NameTableCiram


class Ppu(BusDevice):
    def __init__(self, bus, config):
        self.bus = bus

        self.system_palette = SystemPalette.from_file(config['palette_file'])
        self.bus.add_device(PaletteRam())
        self.bus.add_device(NameTableCiram())

        self.pattern_tables = []

        self.sprites = []

    def handle_read_request(self, request):
        pass

    def handle_write_request(self, request):
        pass
