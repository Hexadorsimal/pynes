from nes import Nes, Cartridge


if __name__ == '__main__':
    nes = Nes()
    cart = Cartridge.create('nestest.nes')

    nes.insert_cartridge(cart)
    nes.power_up()
