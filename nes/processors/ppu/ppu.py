import sys
import pygame

from .palettes.system_palette import SystemPalette
from ..processor import Processor
from .name_table import NameTable
from .pattern_table import PatternTable
from nes.processors.registers import GeneralPurposeRegister
from .ppu_register_set import PpuRegisterSet
from nes.bus.devices.memory import Ram
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

        pygame.init()
        pygame.display.set_caption('PyNES')
        self.screen = pygame.display.set_mode((256, 240))

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

    def draw_background(self):
        pass

    def draw_scanline(self, number):
        for tile in range(32):
            self.draw_tile()

    def draw_tile(self):
        # read nametable byte
        # read attribute table byte
        # read pattern table bitmap #0
        # read pattern table bitmap #1
        pass

    def power_on(self):
        pass

    def tick(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # self.draw_system_palette(0, 0, 8)
        # self.draw_palettes(0, 40, 8)

        for scanline in range(262):
            self.draw_scanline(scanline)

        pygame.display.flip()

        super().tick()
