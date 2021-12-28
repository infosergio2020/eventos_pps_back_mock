from utils.db import db

class Video(db.Model):
    idfoto= db.Column(db.Integer, primary_key=True)
    titulov= db.Column(db.String(45),nullable=False,unique=True)
    urlv= db.Column(db.String(150),nullable=False,unique=True)
    descv= db.Column(db.String(250),nullable=False)


    def __init__(self,titulov, urlv, descv):
        self.titulov = titulov
        self.urlv = urlv
        self.descv = descv