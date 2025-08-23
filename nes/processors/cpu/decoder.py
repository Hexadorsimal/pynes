from dataclasses import dataclass
from sqlite3 import Connection, Row


@dataclass
class Opcode:
    opcode: int
    name: str
    addressing_mode: str
    base_cycles: int
    page_cycles: int
    param_count: int


class Decoder:
    def __init__(self):
        self.conn = Connection('nes.sqlite')
        self.conn.row_factory = Row

    def __del__(self):
        self.conn.close()

    def decode(self, byte: int) -> Opcode:
        c = self.conn.cursor()

        query = (
            'SELECT opcode,'
            '       Instruction.name,'
            '       addressing_mode,'
            '       base_cycles,'
            '       page_cycles,'
            '       param_count '
            '  FROM Instruction JOIN AddressingMode ON Instruction.addressing_mode = AddressingMode.name '
            ' WHERE opcode=?'
        )

        c.execute(query, [byte])
        row = c.fetchone()
        if row:
            result = dict(zip(row.keys(), row))
            return Opcode(**result)
        else:
            raise NotImplementedError(f'Undocumented Opcode: {byte}')
