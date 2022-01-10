
from config.db import db
from models.foto import Foto

class Area(db.Model):
    idarea = db.Column(db.Integer, primary_key=True)
    nomarea = db.Column(db.String(45),nullable=False,unique=True)
    descarea = db.Column(db.String(250),nullable=False)

    # RELACION ONETOMANY CHILD (con evento)
    evento_id = db.Column(db.Integer, db.ForeignKey('evento.idevento'), comment="evento del area i", nullable=True)
    # RELACION ONETOMANY PARENT (con foto)
    fotos = db.relationship("Foto", cascade="all, delete")

    def save(self):
        """ se agrega a la base de datos"""
        if not self.idarea:
            db.session.add(self)
        db.session.commit()

    def remove(self):
        """ se elimina de la base de datos"""
        if self.idarea:
            db.session.delete(self)
            db.session.commit()

    def agregar_foto(self,titulo,url,descripcion):
        """ agrega un area al evento"""
        Foto(  
                titulof= titulo,
                urlf= url,
                descf= descripcion,
                evento = self.idarea ).save()


    #  METODOS STATICOS NO REQUIEREN INSTANCIA PARA USARLOS

    @staticmethod
    def update(id, nombre, descripcion ):
        """ permite actualizar este objeto en la bd , retorna el usuario que actualizó sino retorna None"""
        area = Area.query.get(id) #buscar en la bd
        if area:
            area.nomarea = nombre
            area.descarea = descripcion
            area.save()
            return area
        return None

    @staticmethod
    def delete(id):
        """ dado un id los busca y si existe lo eliminar, retorna el usuario que eliminó sino retorna None"""
        area = Area.query.get(id)
        if area:
            area.remove()
            return area
        return None

    @staticmethod
    def search(search_query, page, per_page):
        """ busca un usuario por name"""
        query = Area.query
        if (search_query):
            query = query.filter(Area.name.like(f"%{search_query}%"))
        return query.paginate(page=page, per_page=per_page, error_out=False)

    @staticmethod
    def all():
        """trae a todos los usuarios"""
        return Area.query.all()

    @staticmethod
    def get_by_id(id):
        """ busca usuario por id"""
        return Area.query.get(id)

    @staticmethod
    def find_by_name(nombre):
        """ busca un usuario por email """
        return Area.query.filter_by(nomarea = nombre).first()

    @staticmethod
    def all_areas(evento_id):
        """ devuelve todas las areas relacionadas a un evento """
        return Area.query.filter(Area.evento_id == evento_id).all()

    @property
    def serialize(self):
       """Return object data in easily serializable format"""
       return {
           "id":self.idarea,
           "nombre": self.nomarea,
           "descripcion": self.descarea
       }