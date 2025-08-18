from dataclasses import dataclass
from sqlite3 import Connection, Row

from nes.processors.cpu.instructions import AddressingMode


@dataclass
class Opcode:
    opcode: int
    name: str
    addressing_mode: AddressingMode
    base_cycles: int
    page_cycles: int
    hex: str


class Decoder:
    def __init__(self):
        self.conn = Connection('nes.sqlite')
        self.conn.row_factory = Row

    def __del__(self):
        self.conn.close()

    def decode(self, byte: int) -> Opcode:
        c = self.conn.cursor()
        c.execute('select * from instruction where opcode=?', [byte])
        row = c.fetchone()
        if row:
            result = dict(zip(row.keys(), row))
            return Opcode(**result)
        else:
            raise NotImplementedError(f'Undocumented Opcode: {byte}')
