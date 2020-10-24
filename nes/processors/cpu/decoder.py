from sqlite3 import Connection, Row


class Decoder:
    def __init__(self):
        self.conn = Connection('nes.sqlite')
        self.conn.row_factory = Row

    def __del__(self):
        self.conn.close()

    def decode(self, opcode):
        c = self.conn.cursor()
        c.execute('select * from instruction where opcode=?', [opcode])
        row = c.fetchone()
        if row:
            return dict(zip(row.keys(), row))
        else:
            raise NotImplementedError('Undocumented Opcode: ' + str(opcode))
