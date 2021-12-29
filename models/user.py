from werkzeug.security import generate_password_hash, check_password_hash
from utils.db import db

class User(db.Model):
    iduser= db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String(45))
    password= db.Column(db.String(125))
    email= db.Column(db.String(125), unique=True)

    def __init__(self,name,password,email):
        self.name=name
        self.set_password(password)
        self.email=email

    def set_password(self, password):
        """settea la contraseña generando un hash para que no se pueda ver"""
        self.password = generate_password_hash(password)

    def check_password(self, password):
        """desencripta la contraseña y la compara, retorna true si coinciden"""
        return check_password_hash(self.password, password)

    def save(self):
        """ se agrega a la base de datos"""
        if not self.iduser:
            db.session.add(self)
        db.session.commit()

    def remove(self):
        """ se elimina de la base de datos"""
        if self.iduser:
            db.session.delete(self)
            db.session.commit()

    def __repr__(self):
        """ retorna un string que describe el objeto """
        return f'<User {self.email}>'

    #  METODOS STATICOS NO REQUIEREN INSTANCIA PARA USARLOS

    @staticmethod
    def update(id, name, password, email ):
        """ permite actualizar este objeto en la bd , retorna el usuario que actualizó sino retorna None"""
        user = User.query.get(id) #buscar en la bd
        if user:
            user.name = name
            user.email = email
            if password:
                user.set_password(password)
            user.save()
            return user
        return None

    @staticmethod
    def delete(id):
        """ dado un id los busca y si existe lo eliminar, retorna el usuario que eliminó sino retorna None"""
        user = User.query.get(id)
        if user:
            user.remove()
            return user
        return None

    @staticmethod
    def search(search_query, page, per_page):
        """ busca un usuario por name"""
        query = User.query
        if (search_query):
            query = query.filter(User.name.like(f"%{search_query}%"))
        return query.paginate(page=page, per_page=per_page, error_out=False)

    @staticmethod
    def all():
        """trae a todos los usuarios"""
        return User.query.all()

    @staticmethod
    def get_by_id(id):
        """ busca usuario por id"""
        return User.query.get(id)

    @staticmethod
    def find_by_email(email):
        """ busca un usuario por email """
        return User.query.filter_by(email = email).first()

    @property
    def serialize(self):
       """Return object data in easily serializable format"""
       return {
           "id":self.iduser,
           "nombre": self.name,
           "email":self.email,
           "contraseña":self.password
       }