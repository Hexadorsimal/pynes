from .. import db


class Instruction(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    description = db.Column(db.String)

    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __repr__(self):
        return '<Instruction {name}>'.format(name=self.name)
