from nes.processors.cpu.registers import Register


class PpuData(Register):
    def read(self):
        # read from vram at the address in PPUADDR
        # increment PPUADDR by amount specified in PPUCTRL
        return 0

    def write(self, data):
        # write data to vram at the address in PPUADDR
        # increment PPUADDR by amount specified in PPUCTRL
        pass
