from flask import Blueprint, request, jsonify
from controller.api import redsocial as red
from models.redsocial import Redsocial #para añadir los datos a la tabla
redsocial= Blueprint('redsocial',__name__)

#Defino la ruta para mostrar la impresion
@redsocial.route('/')
def index():
    return red.index()

#DEFINO LA RUTA PARA RETORNAR UN JSON CON TODOS LOS USUARIOS
@redsocial.route('/redsocial_json')
def redsocial_json():
    return red.redsocial_json()

@redsocial.route('/redsocial_json_by_id/<id>')
def redsocial_json_byId(id):
    return red.redsocial_json_byId(id)

@redsocial.route('/redsocial_json_by_name/<name>')
def redsocial_json_byname(name):
    return red.redsocial_json_byname(name)

#Defino la ruta para crear un contacto
@redsocial.route('/redsocial_add', methods=['POST'])
def redsocial_create():
    return red.redsocial_create()
#Defino la ruta para actualizar un contacto
@redsocial.route('/redsocial_update/<id>',methods=['PUT'])
def redsocial_update(id):
    return red.redsocial_update(id)

#Defino la ruta para eliminar un contacto
@redsocial.route('/redsocial_delete/<id>', methods=['DELETE'])
def redsocial_delete(id):
    return red.redsocial_delete(id)
