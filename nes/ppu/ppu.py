class Ppu:
    def __init__(self):
        self.ppu_controller = 0
        self.ppu_mask = 0
        self.ppu_status = 0
        self.oam_address = 0
        self.oam_data = 0
        self.ppu_scroll = 0
        self.ppu_address = 0
        self.ppu_data = 0
