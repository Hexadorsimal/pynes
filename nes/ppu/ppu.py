from .color import ColorPalette


class Ppu:
    def __init__(self, config):
        self.color_palette = ColorPalette.from_file(config['palette_file'])
        self.universal_background_color = None
        self.background_color_sets = []
        self.sprite_color_sets = []
