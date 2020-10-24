from nes.bus import BusDevice, ReadResponse, WriteResponse


class PaletteRam(BusDevice):
    def __init__(self):
        self.palette = bytearray(32)

    def handle_read_request(self, request):
        if 0x3F00 <= request.addr <= 0x3FFF:
            addr = request.addr & 0x001F
            if addr & 0x03:
                return ReadResponse(request, self, self.palette[addr])
            else:
                return ReadResponse(request, self, self.palette[0])

    def handle_write_request(self, request):
        if 0x3F00 <= request.addr <= 0x3FFF:
            addr = request.addr & 0x001F
            self.palette[addr] = request.data
            return WriteResponse(request, self)
