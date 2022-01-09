from config.db import db
from leng_develop import lenguajes_programador

class Programador(db.model):
    id = db.Column(db.Integer, primary_key= True)
    nombre = db.column(db.String(30))
    edad = db.Colimn(db.Integer)
    empresa_id = db.Column(db.Integer, db.ForeignKey('empresa.id'))

    # RELACION
    empresa = db.Relationship('Empresa', backref = db.backref('programador', lazy=True))
    lenguajes = db.Relationship('Lenguaje', secondary = lenguajes_programador, backref = db.backref('programadores', lazy=True) )

# METODOS PARA AUTOMATIZAR BORRADO/ESCRITURA DE LA CLASE 
    def save(self):
            """ GUARDA Y COMMITEA CAMBIOS EN LA BD"""
            if not self.id:
                db.session.add(self)
            db.session.commit()
    def remove(self):
        """ BORRA Y COMMITEA CAMBIOS EN LA BD"""
        if self.id:
            # self.areas.do(lambda each: each.remove())
            db.session.delete(self)
            db.session.commit()
    @staticmethod
    def update(id, nombre = None, edad = None ):
        """ permite actualizar este objeto en la bd , retorna el usuario que actualizó sino retorna None"""
        programador = Programador.query.get(id) #buscar en la bd
        if programador:
            if nombre:
                programador.nombre = nombre
            if edad:
                programador.edad = edad
            programador.save()
            return programador
        return None
    @staticmethod
    def delete(id):
        """ dado un id los busca y si existe lo eliminar, retorna el usuario que eliminó sino retorna None"""
        programador = Programador.query.get(id)
        if programador:
            programador.remove()
            return programador
        return None
    @staticmethod
    def all():
        """trae a todos los usuarios"""
        return Programador.query.all()
    @staticmethod
    def get_by_id(id):
        """ busca usuario por id"""
        return Programador.query.get(id)
    @property
    def serialize(self):
       """Return object data in easily serializable format"""   
       return {
           "id":self.idevento,
           "nombre": self.nombre,
           "edad": self.edad
       }

    def __repr__(self):
        return f'{self.nombre}'