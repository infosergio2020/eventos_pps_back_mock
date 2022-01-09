from config.db import db

class Empresa(db.model):

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(20))
    fundacion = db.Column(db.Integer, nullable=True)

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
    def update(id, nombre = None, fundacion = None):
        """ permite actualizar este objeto en la bd , retorna el usuario que actualizó sino retorna None"""
        empresa = Empresa.query.get(id) #buscar en la bd
        if empresa:
            if nombre:
                empresa.nombre = nombre
            if fundacion:
                empresa.fundacion = fundacion
            empresa.save()
            return empresa
        return None
    @staticmethod
    def delete(id):
        """ dado un id los busca y si existe lo eliminar, retorna el usuario que eliminó sino retorna None"""
        empresa = Empresa.query.get(id)
        if empresa:
            empresa.remove()
            return empresa
        return None
    @staticmethod
    def all():
        """trae a todos los usuarios"""
        return Empresa.query.all()
    @staticmethod
    def get_by_id(id):
        """ busca usuario por id"""
        return Empresa.query.get(id)
    @property
    def serialize(self):
       """Return object data in easily serializable format"""
       
       return {
           "id":self.idevento,
           "nombre": self.nombre,
           "fundacion": self.fundacion
       }
