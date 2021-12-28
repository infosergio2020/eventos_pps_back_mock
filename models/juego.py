from utils.db import db

class Juego(db.Model):
    idjuego = db.Column(db.Integer, primary_key=True)
    nomjuego = db.Column(db.String(45),nullable=False,unique=True)
    urljuego = db.Column(db.String(150),nullable=False,unique=True)
    urlimgjuego = db.Column(db.String(150),nullable=False,unique=True)
    descjuego = db.Column(db.String(250),nullable=False)

    def __init__(self,nomjuego,urljuego,urlimgjuego,descjuego):
        self.nomjuego = nomjuego
        self.urljuego = urljuego
        self.urlimgjuego = urlimgjuego
        self.descjuego = descjuego