from nes import Nes, Cartridge


if __name__ == '__main__':
    nes = Nes.create('nes.yaml')
    cart = Cartridge.create('donkey-kong.nes')

    nes.insert_cartridge(cart)
    nes.power_up()
