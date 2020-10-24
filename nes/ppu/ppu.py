import sys
import pygame

from nes.bus import BusDevice, ReadRequest, WriteRequest
from .system_palette import SystemPalette


class Ppu(BusDevice):
    def __init__(self, bus, config):
        self.bus = bus
        self.system_palette = SystemPalette.from_file(config['palette_file'])
        self.pattern_tables = []
        self.sprites = []

        pygame.init()
        pygame.display.set_caption('NES Palette')
        self.screen = pygame.display.set_mode((256, 240))

    def handle_read_request(self, request):
        pass

    def handle_write_request(self, request):
        pass

    def draw_pixel(self, x, y, color, size=1):
        rgb = self.system_palette.colors[color]
        pixel = pygame.Rect(x, y, size, size)
        self.screen.fill(rgb, pixel)

    def draw_system_palette(self, left, top, size):
        for y in range(4):
            for x in range(16):
                self.draw_pixel(left + x * size, top + y * size, y * 16 + x, size)

    def draw_palettes(self, left, top, size):
        for y in range(2):
            for x in range(16):
                offset = y * 16 + x
                color = self.bus.read(0x3F00 + offset)
                self.draw_pixel(left + x * size, top + y * size, color, size)

    def tick(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        self.draw_system_palette(0, 0, 8)
        self.draw_palettes(0, 40, 8)

        pygame.display.flip()
