from .memory import Memory


class MemoryMap(Memory):
    def __init__(self, size):
        super().__init__(size)
        self.entries = {}

    def add_memory(self, address_range, memory):
        self.entries[address_range] = memory

    def _find_memory(self, logical_addr):
        for address_range, memory in self.entries:
            if logical_addr in address_range:
                virtual_addr = logical_addr - address_range.start
                local_addr = virtual_addr % memory.size
                return memory, local_addr
        raise ValueError

    def read(self, logical_addr):
        memory, local_addr = self._find_memory(logical_addr)
        return memory.read(local_addr)

    def write(self, logical_addr, value):
        memory, local_addr = self._find_memory(logical_addr)
        memory.write(local_addr, value)
