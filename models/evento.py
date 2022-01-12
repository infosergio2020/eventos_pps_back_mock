import datetime
from config.db import db
from datetime import datetime
from models.area import Area
from models.redsocial import Redsocial
from models.foto import Foto
from models.video import Video

class Evento(db.Model):
    idevento = db.Column(db.Integer, primary_key=True)
    nomevento = db.Column(db.String(45),nullable=False,unique=True)
    lugarevento = db.Column(db.String(150),nullable=False)
    descevento = db.Column(db.String(250),nullable=False)
    fechaevento = db.Column(db.Date,nullable=False)
    horaevento = db.Column(db.Time,nullable=False)
    # implementacion de relacion 1 a muchos
    
    # ONETOMANY PARENT (con area)
    areas = db.relationship("Area", back_populates="evento", cascade="all, delete")
    # ONETOMANY PARENT (con red_social)
    redes = db.relationship("Redsocial", back_populates="evento", cascade="all, delete")
    # ONETOMANY PARENT (con foto)
    fotos = db.relationship("Foto", back_populates="evento", cascade="all, delete")
    # ONETOMANY PARENT (con foto)
    videos = db.relationship("Video", back_populates="evento", cascade="all, delete")

    def __init__(self,nomevento,lugarevento,descevento, fechaevento, horaevento):
        self.nomevento = nomevento
        self.lugarevento = lugarevento
        self.descevento = descevento
        self.fechaevento = fechaevento
        self.horaevento = horaevento
        self.areas = []
        self.redes = []
        self.fotos = []
        self.videos = []

    def save(self):
        """ se agrega a la base de datos"""
        if not self.idevento:
            db.session.add(self)
        db.session.commit()

    def remove(self):
        """ se elimina de la base de datos"""
        if self.idevento:
            # self.areas.do(lambda each: each.remove())
            db.session.delete(self)
            db.session.commit()

    def agregar_area(self,nombre,descripcion):
        """ agrega un area al evento"""
        Area(   nomarea = nombre,
                descarea = descripcion, 
                evento = self).save()
                
    def agregar_red(self,nombre):
        """ agrega un area al evento"""
        Redsocial(  nombrered = nombre,
                    evento = self ).save()

    def agregar_foto(self,titulo,url,descripcion):
        """ agrega un area al evento"""
        Foto(  
                titulof= titulo,
                urlf= url,
                descf= descripcion,
                evento = self ).save() 

    def agregar_video(self,titulo,url,descripcion):
        """ agrega un area al evento"""
        Video(  
                titulov= titulo,
                urlv= url,
                descv= descripcion,
                evento = self ).save()
    

    #  METODOS STATICOS NO REQUIEREN INSTANCIA PARA USARLOS
    @staticmethod
    def update(id, nombre, lugar, descripcion, fecha, hora ):
        """ permite actualizar este objeto en la bd , retorna el usuario que actualizó sino retorna None"""
        evento = Evento.query.get(id) #buscar en la bd
        if evento:
            evento.nomevento = nombre
            evento.lugarevento = lugar
            evento.descevento = descripcion
            evento.fechaevento = fecha
            evento.horaevento = hora
            evento.save()
            return evento
        return None

    @staticmethod
    def delete(id):
        """ dado un id los busca y si existe lo eliminar, retorna el usuario que eliminó sino retorna None"""
        evento = Evento.query.get(id)
        if evento:
            evento.remove()
            return evento
        return None

    @staticmethod
    def search(search_query, page, per_page):
        """ busca un usuario por name"""
        query = Evento.query
        if (search_query):
            query = query.filter(Evento.name.like(f"%{search_query}%"))
        return query.paginate(page=page, per_page=per_page, error_out=False)

    @staticmethod
    def all():
        """trae a todos los usuarios"""
        return Evento.query.all()

    @staticmethod
    def get_by_id(id):
        """ busca usuario por id"""
        return Evento.query.get(id)

    @staticmethod
    def find_by_name(nombre):
        """ busca un usuario por email """
        return Evento.query.filter_by(nomevento = nombre).first()

    @property
    def serialize(self):
       """Return object data in easily serializable format"""
       combinado = datetime.combine(self.fechaevento,self.horaevento)
       return {
           "id":self.idevento,
           "nombre": self.nomevento,
           "lugar": self.lugarevento,
           "descripcion": self.descevento,
           "fecha": combinado.strftime("%Y/%m/%d"),
           "hora": combinado.strftime("%H:%M:%S"),
           "cantidad_areas": len(self.areas)
       }