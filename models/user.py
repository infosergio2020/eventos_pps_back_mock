from utils.db import db

class User(db.Model):
    iduser= db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String(45))
    password= db.Column(db.String(125))
    email= db.Column(db.String(125), unique=True)

    def __init__(self,name,password,email):
        self.name=name
        self.password=password
        self.email=email
