from utils.db import db

class Foto(db.Model):
    idfoto= db.Column(db.Integer, primary_key=True)
    titulof= db.Column(db.String(45),nullable=False,unique=True)
    urlf= db.Column(db.String(150),nullable=False,unique=True)
    descf= db.Column(db.String(250),nullable=False)


    def __init__(self,titulof, urlf, descf):
        self.titulof = titulof
        self.urlf = urlf
        self.descf = descf

    def save(self):
        """ se agrega a la base de datos"""
        if not self.idfoto:
            db.session.add(self)
        db.session.commit()

    def remove(self):
        """ se elimina de la base de datos"""
        if self.idvideo:
            db.session.delete(self)
            db.session.commit()

    #  METODOS STATICOS NO REQUIEREN INSTANCIA PARA USARLOS

    @staticmethod
    def update(id, titulo,url,descripcion):
        """ permite actualizar este objeto en la bd , retorna el usuario que actualizó sino retorna None"""
        foto = Foto.query.get(id) #buscar en la bd
        if foto:
            foto.titulof = titulo
            foto.urlf = url
            foto.descf = descripcion
            foto.save()
            return foto
        return None

    @staticmethod
    def delete(id):
        """ dado un id los busca y si existe lo eliminar, retorna el usuario que eliminó sino retorna None"""
        foto = Foto.query.get(id)
        if foto:
            foto.remove()
            return foto
        return None

    @staticmethod
    def search(search_query, page, per_page):
        """ busca un usuario por name"""
        query = Foto.query
        if (search_query):
            query = query.filter(Foto.name.like(f"%{search_query}%"))
        return query.paginate(page=page, per_page=per_page, error_out=False)

    @staticmethod
    def all():
        """trae a todos los usuarios"""
        return Foto.query.all()

    @staticmethod
    def get_by_id(id):
        """ busca usuario por id"""
        return Foto.query.get(id)

    @staticmethod
    def find_by_titulo(titulo):
        """ busca un usuario por email """
        return Foto.query.filter_by(tituloF = titulo).first()

    @property
    def serialize(self):
       """Return object data in easily serializable format"""
       return {
           "id":self.idfoto,
           "titulo": self.titulof,
           "url": self.urlf,
           "descripcion": self.descf
       }