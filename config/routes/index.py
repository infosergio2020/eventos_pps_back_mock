from controller.api import index as i
from flask import Blueprint
index = Blueprint('index',__name__)
#Defino la ruta para mostrar la impresion

# Web API uses appropriate HTTP verbs for each action:
# --------------------------------------------------------
# METHOD  |    ACTION
# GET     |  Retrieves resources
# POST    |  Creates resources
# PUT     |  Changes and/or replaces resources or collections
# DELETE  |  Deletes resources
# --------------------------------------------------------


# #DEFINO LA RUTA PARA RETORNAR UN JSON CON TODOS LOS USUARIOS
@index.route('/index/')
def indexF():
    return i.indexF()