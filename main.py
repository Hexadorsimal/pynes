import yaml
from nes import Nes, CartridgeFactory


if __name__ == '__main__':
    config = yaml.load(open('config.yaml', 'rt'), Loader=yaml.FullLoader)

    cart = CartridgeFactory.create('donkey-kong.nes')

    nes = Nes(config)
    nes.insert_cartridge(cart)

    for i in range(32):
        nes.ppu.bus.write(0x3F00 + i, i)

    nes.power_up()
