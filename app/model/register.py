from .. import db


class Register(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    description = db.Column(db.String)
    type = db.Column(db.String)

    def __init__(self, name, description, type=None):
        self.name = name
        self.description = description
        self.type = type
