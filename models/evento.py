from utils.db import db

class Evento(db.Model):
    idevento = db.Column(db.Integer, primary_key=True)
    nomevento = db.Column(db.String(45),nullable=False,unique=True)
    lugarevento = db.Column(db.String(150),nullable=False)
    descevento = db.Column(db.String(250),nullable=False)
    fechaevento = db.Column(db.Date,nullable=False)
    horaevento = db.Column(db.Time,nullable=False)

    def __init__(self,nomevento,lugarevento,descevento, fechaevento, horaevento):
        self.nomevento = nomevento
        self.lugarevento = lugarevento
        self.descevento = descevento
        self.fechaevento = fechaevento
        self.horaevento = horaevento