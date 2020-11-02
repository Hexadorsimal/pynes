from nes.processors.registers import Register


class OamDma(Register):
    def __init__(self, ppu, cpu):
        self.ppu = ppu
        self.cpu = cpu

    def read(self):
        raise RuntimeError('OAMDMA is a write-only register')

    @property
    def value(self):
        return None

    @value.setter
    def value(self, cpu_mem_page):
        cpu_mem_addr = cpu_mem_page << 8

        # copy 256 bytes of data from cpu memory to ppu oam memory starting at oamaddr
        for addr in range(256):
            data = self.cpu.read(cpu_mem_page | addr)
            self.ppu.oam.write(data)
