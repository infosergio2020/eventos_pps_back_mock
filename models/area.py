from utils.db import db
from models.user import User

from sqlalchemy import Column, Integer, String, DateTime, Boolean, TIMESTAMP, func
from sqlalchemy.orm import relationship

# from sqlalchemy_demo.connect import Base
from sqlalchemy import ForeignKey

class Area(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String(45))
    # Usuarios=evento
    # agrego relacion con empresa Uno a muchos (1 evento--> muchas areas)
    # empresa_id=db.Column(db.Integer, db.ForeignKey('empresa.id'))
    # empresa= db.relationship('Empresa',backref=db.backref('users',lazy=True))




    # # Asociación de clave externa (el tipo de clave asociada debe ser el mismo que el tipo definido)
    # user_id = Column(Integer, ForeignKey(User.iduser), comment='Evento del area i')

    # Al asociarse para que la información de la tabla de usuario se pueda obtener en la página de la lista de artículos
    # user = relationship(User, back_populates='area')
    
    
    def __init__(self,name):
        self.name=name
    
    @staticmethod
    def all():
        """trae a todas las areas"""
        return Area.query.all()
    
