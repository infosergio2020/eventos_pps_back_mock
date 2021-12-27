# comienzo
from flask import Flask
from routes.user import user #quiero probar la ruta de usuario
from routes.evento import evento
from flask_sqlalchemy import SQLAlchemy

class MyApp:
    def __init__(self, ):
        ##Configuracion del app
        self._app= Flask(__name__)
        # from flask_marshmallow import Marshmallow
        # from werkzeug.exceptions import MethodNotAllowed
        self._app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:admin123@127.0.0.1:3306/eventos'
        self._app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
        SQLAlchemy(self._app) #le paso al ORM la configuracion que posee el self._app
        #Configuracion del self._app

        self._app.register_blueprint(user) #invoco las rutas del usuario
        self._app.register_blueprint(evento)
    
    def get_app(self):
        return self._app




# ma=Marshmallow(app) #instanciar un esquema


# db.create_all() #crea las tablas

# #esquema para interactuar
# class UserSchema(ma.Schema):
#     class Meta:
#         fields=('id','name','password','email')
# user_schema= UserSchema() #esquema user instanciado
# users_schema= UserSchema(many=True) #esquema devarios usuarios instanciadps

# #Defino la ruta para crear el user
# @app.route('/users',methods=['POST'])
# def create_user():
#     print(request.json)
#     return 'received'



