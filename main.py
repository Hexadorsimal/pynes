from nes import Nes


if __name__ == '__main__':
    nes = Nes.create('nes/cpu/6502.yaml')
    nes.load_cartridge('donkey-kong.nes')
    nes.power_up()
