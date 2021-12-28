# comienzo
from flask import Flask
from routes.user import user #quiero probar la ruta de usuario
from routes.evento import evento
from flask_sqlalchemy import SQLAlchemy
from entorno import config

##Configuracion del app
app = Flask(__name__)
app.secret_key="secret key" # configuro un valor para que se genere una sesion
app.config.from_object(config)
SQLAlchemy(app) #le paso al ORM la configuracion que posee el app  #Configuracion del app
app.register_blueprint(user) #invoco las rutas del usuario
app.register_blueprint(evento)
    