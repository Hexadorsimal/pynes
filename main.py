from nes import Nes


if __name__ == '__main__':
    nes = Nes.load('nes/cpu/6502.yaml')
    nes.power_up()
