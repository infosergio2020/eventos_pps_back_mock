# comienzo
from flask import Flask
from config.routes.index import index

from flask_sqlalchemy import SQLAlchemy
from config.entorno import config

##Configuracion del app
app = Flask(__name__)
app.secret_key="secret key" # configuro un valor para que se genere una sesion
app.config.from_object(config)
SQLAlchemy(app) #le paso al ORM la configuracion que posee el app  #Configuracion del app
app.register_blueprint(index) #invoco las rutas del usuario
    