from utils.db import db

class Foto(db.Model):
    idvideo= db.Column(db.Integer, primary_key=True)
    titulof= db.Column(db.String(45),nullable=False,unique=True)
    urlf= db.Column(db.String(150),nullable=False,unique=True)
    descf= db.Column(db.String(250),nullable=False)


    def __init__(self,titulof, urlf, descf):
        self.titulof = titulof
        self.urlf = urlf
        self.descf = descf