from utils.db import db
from sqlalchemy import Date,Time

class Envivo(db.Model):
    idenvivo = db.Column(db.Integer, primary_key=True)
    nomenvivo = db.Column(db.String(45),nullable=False,unique=True)
    urlenvivo = db.Column(db.String(150),nullable=False,unique=True)
    descenvivo = db.Column(db.String(250),nullable=False)
    fechaenvivo = db.Column(db.Date,nullable=False)
    horaenvivo = db.Column(db.Time,nullable=False)

    def __init__(self,nomenvivo,urlenvivo,descenvivo, fechaenvivo, horaenvivo):
        self.nomenvivo = nomenvivo
        self.urlenvivo = urlenvivo
        self.descenvivo = descenvivo
        self.fechaenvivo = fechaenvivo
        self.horaenvivo = horaenvivo