from .ines import iNesHeader
from .trainer import Trainer
from .playchoice10 import PlayChoice10


class RomFile:
    def __init__(self, filename, header, prg_rom, chr_rom, prg_ram, trainer, pc10, extra):
        self.filename = filename
        self.header = header
        self.prg_rom_pages = prg_rom
        self.chr_rom_pages = chr_rom
        self.prg_ram_pages = prg_ram
        self.trainer = trainer
        self.playchoice10 = pc10
        self.extra = extra

    @staticmethod
    def load(filename):
        with open(filename, 'rb') as f:
            header = iNesHeader(f.read(16))
            trainer = None
            if header.contains_trainer:
                trainer = Trainer(f.read(512))

            prg_rom_pages = []
            for page in range(header.prg_rom_page_count):
                prg_rom_pages.append(f.read(header.prg_rom_page_size))

            chr_rom_pages = []
            for page in range(header.chr_rom_page_count):
                chr_rom_pages.append(f.read(header.chr_rom_page_size))

            pc10 = None
            if header.is_playchoice10:
                inst_rom = f.read(PlayChoice10.inst_rom_size)
                prom_data = f.read(PlayChoice10.prom_data_size)
                prom_counter_out = f.read(PlayChoice10.prom_counter_out_size)
                pc10 = PlayChoice10(inst_rom, prom_data, prom_counter_out)

            remaining_data = f.read()

            return Rom(filename=filename,
                       header=header,
                       prg_rom=prg_rom_pages,
                       chr_rom=chr_rom_pages,
                       prg_ram=None,
                       trainer=trainer,
                       pc10=pc10,
                       extra=remaining_data)
