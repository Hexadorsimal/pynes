class PlayChoice10:
    inst_rom_size = 8 * 1024
    prom_data_size = 16
    prom_counter_out_size = 16
    prom_size = prom_data_size + prom_counter_out_size

    def __init__(self, inst_rom, data, counter_out):
        self.inst_rom = inst_rom
        self.data = data
        self.counter_out = counter_out
