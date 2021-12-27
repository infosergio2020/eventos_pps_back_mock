# comienzo
from flask import Flask
from routes.user import user #quiero probar la ruta de usuario
from routes.evento import evento
from flask_sqlalchemy import SQLAlchemy

##Configuracion del app
app= Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:admin123@127.0.0.1:3306/eventos'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
SQLAlchemy(app) #le paso al ORM la configuracion que posee el app  #Configuracion del app
app.register_blueprint(user) #invoco las rutas del usuario
app.register_blueprint(evento)
    



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



