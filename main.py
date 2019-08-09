import pygame
import yaml
from nes import Nes, CartridgeFactory


if __name__ == '__main__':
    config = yaml.load(open('config.yaml', 'rt'), Loader=yaml.FullLoader)

    cart = CartridgeFactory.create('donkey-kong.nes')

    nes = Nes(config)
    nes.insert_cartridge(cart)
    # nes.power_up()

    for i in range(32):
        nes.ppu.bus.write(0x3F00 + i, i)

    pygame.init()
    pygame.display.set_caption('NES Palette')
    screen = pygame.display.set_mode((256, 240))

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        rect = pygame.Rect(0, 0, 16, 16)
        for color in nes.ppu.system_palette.colors:
            screen.fill(color, rect)
            rect.x += rect.w
            if rect.x >= rect.w * 16:
                rect.x = 0
                rect.y += rect.h

        rect.x = 0
        rect.y = 64

        for i in range(32):
            color_index = nes.ppu.bus.read(0x3F00 + i)
            color = nes.ppu.system_palette.colors[color_index]
            screen.fill(color, rect)
            rect.x += rect.w
            if rect.x >= rect.w * 16:
                rect.x = 0
                rect.y += rect.h

        pygame.display.flip()
