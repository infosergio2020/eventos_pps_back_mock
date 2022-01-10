from config.db import db
from models.foto import Foto

class Juego(db.Model):
    idjuego = db.Column(db.Integer, primary_key=True)
    nomjuego = db.Column(db.String(45),nullable=False,unique=True)
    urljuego = db.Column(db.String(150),nullable=False,unique=True)
    urlimgjuego = db.Column(db.String(150),nullable=False,unique=True)
    descjuego = db.Column(db.String(250),nullable=False)

    # RELACION ONETOMANY PARENT (con foto)
    fotos = db.relationship("Foto", cascade="all, delete")

    def __init__(self,nomjuego,urljuego,urlimgjuego,descjuego):
        self.nomjuego = nomjuego
        self.urljuego = urljuego
        self.urlimgjuego = urlimgjuego
        self.descjuego = descjuego

    def save(self):
        """ se agrega a la base de datos"""
        if not self.idjuego:
            db.session.add(self)
        db.session.commit()

    def remove(self):
        """ se elimina de la base de datos"""
        if self.idjuego:
            db.session.delete(self)
            db.session.commit()

    def agregar_foto(self,titulo,url,descripcion):
        """ agrega un area al evento"""
        Foto(  
                titulof= titulo,
                urlf= url,
                descf= descripcion,
                evento = self.idjuego ).save()

    def __repr__(self):
        """ retorna un string que describe el objeto """
        return f'<redSocial {self.nomjuego}>'

    #  METODOS STATICOS NO REQUIEREN INSTANCIA PARA USARLOS

    @staticmethod
    def update(id, nombre,urljuego,urlimagen,descripcion):
        """ permite actualizar este objeto en la bd , retorna el usuario que actualizó sino retorna None"""
        juego = Juego.query.get(id) #buscar en la bd
        if juego:
            juego.nomjuego = nombre
            juego.urljuego = urljuego
            juego.urlimgjuego = urlimagen
            juego.descjuego = descripcion
            juego.save()
            return juego
        return None

    @staticmethod
    def delete(id):
        """ dado un id los busca y si existe lo eliminar, retorna el usuario que eliminó sino retorna None"""
        juego = Juego.query.get(id)
        if juego:
            juego.remove()
            return juego
        return None

    @staticmethod
    def search(search_query, page, per_page):
        """ busca un usuario por name"""
        query = Juego.query
        if (search_query):
            query = query.filter(Juego.name.like(f"%{search_query}%"))
        return query.paginate(page=page, per_page=per_page, error_out=False)

    @staticmethod
    def all():
        """trae a todos los usuarios"""
        return Juego.query.all()

    @staticmethod
    def get_by_id(id):
        """ busca usuario por id"""
        return Juego.query.get(id)

    @staticmethod
    def find_by_name(nombre):
        """ busca un usuario por email """
        return Juego.query.filter_by(nomjuego = nombre).first()

    @property
    def serialize(self):
       """Return object data in easily serializable format"""
       return {
           "id":self.idjuego,
           "nombre": self.nomjuego,
           "url_juego": self.urljuego,
           "url_img_juego": self.urlimgjuego,
           "descripcion": self.descjuego
       }