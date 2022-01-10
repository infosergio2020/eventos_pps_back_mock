from config.db import db

class Redsocial(db.Model):
    idredsocial = db.Column(db.Integer, primary_key=True)
    nombrered = db.Column(db.String(45), nullable=False,unique=True)
    
    # RELACION ONETOMANY CHILD (con evento)
    evento_id = db.Column(db.Integer, db.ForeignKey('evento.idevento'), comment="evento de la red i", nullable=True)

    def save(self):
        """ se agrega a la base de datos"""
        if not self.idredsocial:
            db.session.add(self)
        db.session.commit()

    def remove(self):
        """ se elimina de la base de datos"""
        if self.idredsocial:
            db.session.delete(self)
            db.session.commit()

    def __repr__(self):
        """ retorna un string que describe el objeto """
        return f'<redSocial {self.nombrered}>'

    #  METODOS STATICOS NO REQUIEREN INSTANCIA PARA USARLOS

    @staticmethod
    def update(id, nombre):
        """ permite actualizar este objeto en la bd , retorna el usuario que actualizó sino retorna None"""
        red = Redsocial.query.get(id) #buscar en la bd
        if red:
            red.nombrered = nombre
            red.save()
            return red
        return None

    @staticmethod
    def delete(id):
        """ dado un id los busca y si existe lo eliminar, retorna el usuario que eliminó sino retorna None"""
        red = Redsocial.query.get(id)
        if red:
            red.remove()
            return red
        return None

    @staticmethod
    def search(search_query, page, per_page):
        """ busca un usuario por name"""
        query = Redsocial.query
        if (search_query):
            query = query.filter(Redsocial.name.like(f"%{search_query}%"))
        return query.paginate(page=page, per_page=per_page, error_out=False)

    @staticmethod
    def all():
        """trae a todos los usuarios"""
        return Redsocial.query.all()

    @staticmethod
    def get_by_id(id):
        """ busca usuario por id"""
        return Redsocial.query.get(id)

    @staticmethod
    def find_by_email(nombre):
        """ busca un usuario por email """
        return Redsocial.query.filter_by(nombrered = nombre).first()

    @staticmethod
    def all_areas(evento_id):
        """ devuelve todas las areas relacionadas a un evento """
        return Redsocial.query.filter(Redsocial.evento_id == evento_id).all()

    @property
    def serialize(self):
       """Return object data in easily serializable format"""
       return {
           "id":self.idevento,
           "nombre": self.nombrered,
       }
