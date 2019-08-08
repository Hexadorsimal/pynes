from .color import SystemPalette


class Ppu:
    def __init__(self, bus, config):
        self.bus = bus

        self.system_palette = SystemPalette.from_file(config['palette_file'])
        self.background_color = None
        self.background_palettes = []
        self.sprite_palettes = []

        self.pattern_tables = []
        self.name_tables = []

        self.sprites = []
