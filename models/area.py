from utils.db import db

class Area(db.Model):
    idarea = db.Column(db.Integer, primary_key=True)
    nomarea = db.Column(db.String(45),nullable=False,unique=True)
    descarea = db.Column(db.String(250),nullable=False)

    def __init__(self,nomarea,descarea):
        self.nomarea = nomarea
        self.descarea = descarea