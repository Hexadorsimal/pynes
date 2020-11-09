from nes.bus.devices.memory import Ram
from nes.processors.registers import GeneralPurposeRegister
from nes.video import Television
from .palettes.system_palette import SystemPalette
from ..processor import Processor
from .name_table import NameTable
from .pattern_table import PatternTable
from .ppu_register_set import PpuRegisterSet
from .registers import PpuAddr, PpuCtrl, PpuData, PpuMask, PpuScroll, PpuStatus, OamAddr, OamData, OamDma


class Ppu(Processor):
    def __init__(self, bus, cpu, config):
        super().__init__(bus)

        self.registers = {
            'nt': GeneralPurposeRegister(),
            'at': GeneralPurposeRegister(),
            'pt': GeneralPurposeRegister(),
            'fv': GeneralPurposeRegister(),
            'fh': GeneralPurposeRegister(),
            'vt': GeneralPurposeRegister(),
            'ht': GeneralPurposeRegister(),
            'v': GeneralPurposeRegister(),
            'h': GeneralPurposeRegister(),
            's': GeneralPurposeRegister(),
            'par': GeneralPurposeRegister(),
            'ar': GeneralPurposeRegister(),
            'ppuctrl': PpuCtrl(),
            'ppumask': PpuMask(),
            'ppustatus': PpuStatus(),
            'ppuscroll': PpuScroll(self),
            'ppuaddr': PpuAddr(),
            'ppudata': PpuData(self),
            'oamaddr': OamAddr(),
            'oamdata': OamData(self),
            'oamdma': OamDma(self, cpu),
        }

        self.register_set = PpuRegisterSet(self)

        self.system_palette = SystemPalette.from_file(config['palette_file'])

        self.pattern_tables = [
            PatternTable(0x0000, 0x1000),
            PatternTable(0x1000, 0x1000),
        ]

        self.name_tables = [
            NameTable(0x2000, 0x0400),
            NameTable(0x2400, 0x0400),
            NameTable(0x2800, 0x0400),
            NameTable(0x2C00, 0x0400),
        ]

        self.oam = Ram(256)

        self.video = Television()

    @property
    def ppuctrl(self):
        return self.registers['ppuctrl']

    @property
    def ppumask(self):
        return self.registers['ppumask']

    @property
    def ppustatus(self):
        return self.registers['ppustatus']

    @property
    def oamaddr(self):
        return self.registers['oamaddr']

    @property
    def oamdata(self):
        return self.registers['oamdata']

    @property
    def oamdma(self):
        return self.registers['oamdma']

    @property
    def ppuscroll(self):
        return self.registers['ppuscroll']

    @property
    def ppuaddr(self):
        return self.registers['ppuaddr']

    @property
    def ppudata(self):
        return self.registers['ppudata']

    def read(self, addr):
        return self.bus.read(addr)

    def write(self, addr, value):
        self.bus.write(addr, value)

    def get_rgb(self, color):
        rgb = self.system_palette.colors[color]
        return rgb

    def power_on(self):
        self.video.power_up()

    def power_off(self):
        self.video.power_down()

    def tick(self):
        x = self.clock % 256
        y = (self.clock // 256) % 240
        color_index = self.clock % 64
        color = self.get_rgb(color_index)

        # print(f'pixel ({x},{y})')
        self.video.pixel(x, y, color)

        if x == 255:
            if y == 239:
                print('VSYNC')
                self.video.vsync()
            else:
                print(f'HSYNC y({y})')
                self.video.hsync()

        super().tick()
