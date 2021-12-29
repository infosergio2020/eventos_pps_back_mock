from utils.db import db
from sqlalchemy import Date,Time

class Envivo(db.Model):
    idenvivo = db.Column(db.Integer, primary_key=True)
    nomenvivo = db.Column(db.String(45),nullable=False,unique=True)
    urlenvivo = db.Column(db.String(150),nullable=False,unique=True)
    descenvivo = db.Column(db.String(250),nullable=False)
    fechaenvivo = db.Column(db.Date,nullable=False)
    horaenvivo = db.Column(db.Time,nullable=False)

    def __init__(self, nombre, url, descripcion, fecha, hora):
        self.nomenvivo = nombre
        self.urlenvivo = url
        self.descenvivo = descripcion
        self.fechaenvivo = fecha
        self.horaenvivo = hora


    def save(self):
        """ se agrega a la base de datos"""
        if not self.idenvivo:
            db.session.add(self)
        db.session.commit()

    def remove(self):
        """ se elimina de la base de datos"""
        if self.idenvivo:
            db.session.delete(self)
            db.session.commit()

    #  METODOS STATICOS NO REQUIEREN INSTANCIA PARA USARLOS

    @staticmethod
    def update(id, nombre, url, descripcion, fecha, hora ):
        """ permite actualizar este objeto en la bd , retorna el usuario que actualizó sino retorna None"""
        envivo = Envivo.query.get(id) #buscar en la bd
        if envivo:
            envivo.nomenvivo = nombre
            envivo.urlenvivo = url
            envivo.descenvivo = descripcion
            envivo.fechaenvivo = fecha
            envivo.horaenvivo = hora
            envivo.save()
            return envivo
        return None

    @staticmethod
    def delete(id):
        """ dado un id los busca y si existe lo eliminar, retorna el usuario que eliminó sino retorna None"""
        envivo = Envivo.query.get(id)
        if envivo:
            envivo.remove()
            return envivo
        return None

    @staticmethod
    def search(search_query, page, per_page):
        """ busca un usuario por name"""
        query = Envivo.query
        if (search_query):
            query = query.filter(Envivo.name.like(f"%{search_query}%"))
        return query.paginate(page=page, per_page=per_page, error_out=False)

    @staticmethod
    def all():
        """trae a todos los usuarios"""
        return Envivo.query.all()

    @staticmethod
    def get_by_id(id):
        """ busca usuario por id"""
        return Envivo.query.get(id)

    @staticmethod
    def find_by_name(nombre):
        """ busca un usuario por email """
        return Envivo.query.filter_by(nomenvivo = nombre).first()

    @property
    def serialize(self):
       """Return object data in easily serializable format"""
       return {
           "id":self.idenvivo,
           "nombre": self.nomenvivo,
           "url": self.urlenvivo,
           "descripcion": self.descenvivo,
           "fecha": self.fechaenvivo,
           "hora": self.horaenvivo
       }