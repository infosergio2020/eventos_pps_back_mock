from config.db import db


class Lenguaje(db.Model):
    id = db.Column(db.Integer, primary_key= True)
    nombre = db.Column(db.String(30))
    creador = db.Column(db.String(30))

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

    #  METODOS STATICOS NO REQUIEREN INSTANCIA PARA USARLOS
    @staticmethod
    def update(id, nombre = None, creador = None):
        """ permite actualizar este objeto en la bd , retorna el usuario que actualizó sino retorna None"""
        lenguaje = Lenguaje.query.get(id) #buscar en la bd
        if lenguaje:
            if nombre:
                lenguaje.nombre = nombre
            if creador:
                lenguaje.creador = creador
            lenguaje.save()
            return lenguaje
        return None
    @staticmethod
    def delete(id):
        """ dado un id los busca y si existe lo eliminar, retorna el usuario que eliminó sino retorna None"""
        lenguaje = Lenguaje.query.get(id)
        if lenguaje:
            lenguaje.remove()
            return lenguaje
        return None
    @staticmethod
    def all():
        """trae a todos los usuarios"""
        return Lenguaje.query.all()
    @staticmethod
    def get_by_id(id):
        """ busca usuario por id"""
        return Lenguaje.query.get(id)
    @property
    def serialize(self):
       """Return object data in easily serializable format"""
       
       return {
           "id":self.idevento,
           "nombre": self.nombre,
           "creador": self.creador
       }
