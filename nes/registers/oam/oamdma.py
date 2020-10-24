from nes.registers.register import Register


class OamDma(Register):
    def read(self):
        raise RuntimeError('OAMDMA is a write-only register')

    def write(self, data):
        cpu_mem_addr = data << 8
        # copy 256 bytes of data from cpu memory to ppu oam memory starting at oamaddr
        pass
