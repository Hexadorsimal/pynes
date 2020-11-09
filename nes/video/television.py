import pygame
from .video_out import VideoOut


class Television(VideoOut):
    def __init__(self):
        self.surface = None
        self.pixels = None

    def power_up(self):
        pygame.init()
        pygame.display.set_caption('PyNES Television')

        self.surface = pygame.display.set_mode((256, 240))
        self.pixels = pygame.PixelArray(self.surface)

    def power_down(self):
        pygame.quit()

    def pixel(self, x, y, color):
        self.pixels[x, y] = color

    def hsync(self):
        pass

    def vsync(self):
        pygame.display.flip()
