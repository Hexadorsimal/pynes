from nes.bus import BusDevice, ReadRequest, WriteRequest, ReadResponse, WriteResponse


class Cartridge(BusDevice):
    def __init__(self, rom_file):
        self.rom_file = rom_file

    def handle_request(self, request):
        if isinstance(request, ReadRequest):
            if request.bus.name == 'cpu':
                return self.handle_cpu_read_request(request)
            elif request.bus.name == 'ppu':
                return self.handle_ppu_read_request(request)
        elif isinstance(request, WriteRequest):
            if request.bus.name == 'cpu':
                return self.handle_cpu_write_request(request)
            elif request.bus.name == 'ppu':
                return self.handle_ppu_write_request(request)

    def handle_cpu_read_request(self, request):
        pass

    def handle_cpu_write_request(self, request):
        pass

    def handle_ppu_read_request(self, request):
        pass

    def handle_ppu_write_request(self, request):
        pass
