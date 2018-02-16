from nes.memory import MemoryMap


class PpuRegisterSet(MemoryMap):
    def __init__(self):
        super().__init__(8)
