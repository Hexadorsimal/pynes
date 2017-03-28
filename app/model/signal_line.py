from .. import db


class SignalLine(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    description = db.Column(db.String)

    def __init__(self, name, description):
        self.name = name
        self.description = description
