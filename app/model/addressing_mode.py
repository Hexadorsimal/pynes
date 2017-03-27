from .. import db


class AddressingMode(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)

    def __init__(self, name):
        self.name = name
