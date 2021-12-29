from utils.db import db

class Video(db.Model):
    idvideo= db.Column(db.Integer, primary_key=True)
    titulov= db.Column(db.String(45),nullable=False,unique=True)
    urlv= db.Column(db.String(150),nullable=False,unique=True)
    descv= db.Column(db.String(250),nullable=False)

    def __init__(self,titulov, urlv, descv):
        self.titulov = titulov
        self.urlv = urlv
        self.descv = descv
    
    def save(self):
        """ se agrega a la base de datos"""
        if not self.idvideo:
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
        video = Video.query.get(id) #buscar en la bd
        if video:
            video.titulov = titulo
            video.urlv = url
            video.descv = descripcion
            video.save()
            return video
        return None

    @staticmethod
    def delete(id):
        """ dado un id los busca y si existe lo eliminar, retorna el usuario que eliminó sino retorna None"""
        videos = Video.query.get(id)
        if videos:
            videos.remove()
            return videos
        return None

    @staticmethod
    def search(search_query, page, per_page):
        """ busca un usuario por name"""
        query = Video.query
        if (search_query):
            query = query.filter(Video.name.like(f"%{search_query}%"))
        return query.paginate(page=page, per_page=per_page, error_out=False)

    @staticmethod
    def all():
        """trae a todos los usuarios"""
        return Video.query.all()

    @staticmethod
    def get_by_id(id):
        """ busca usuario por id"""
        return Video.query.get(id)

    @staticmethod
    def find_by_titulo(titulo):
        """ busca un usuario por email """
        return Video.query.filter_by(tituloF = titulo).first()

    @property
    def serialize(self):
       """Return object data in easily serializable format"""
       return {
           "id":self.idvideo,
           "titulo": self.titulov,
           "url": self.urlv,
           "descripcion": self.descv
       }