from controller.api import evento as e
from flask import Blueprint
evento = Blueprint('evento',__name__)
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
@evento.route('/evento/')
def index():
    return e.index()

@evento.route('/evento/get-all')
def evento_json():
    return e.evento_json()

@evento.route('/evento/get-by-id/<id>')
def evento_json_byId():
    return e.evento_json_byId

@evento.route('/evento/get-by-name/<name>')
def evento_json_byname():
    return e.evento_json_byname()

#Defino la ruta para crear un contacto
@evento.route('/evento/add', methods=['POST'])
def evento_create():
    return e.evento_create()

#Defino la ruta para actualizar un contacto
@evento.route('/evento/update/<id>',methods=['PUT'])
def evento_update(id):
    return e.evento_update(id)

#Defino la ruta para eliminar un contacto
@evento.route('/evento/delete/<id>',methods =['DELETE'])
def evento_delete(id):
    return e.evento_delete(id)