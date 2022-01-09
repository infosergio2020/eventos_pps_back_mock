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


    def __repr__(self):
        return f'{self.nombre}'