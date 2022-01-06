from controller.api import area as a
from flask import Blueprint
area= Blueprint('area',__name__)

#Defino la ruta para mostrar la impresion
@area.route('/')
def index():
    return a.index()

#DEFINO LA RUTA PARA RETORNAR UN JSON CON TODOS LOS USUARIOS
@area.route('/area_json')
def area_json():
    return a.area_json()

@area.route('/area_json_by_id/<id>')
def area_json_byId(id):
    return a.area_json_byId(id)

@area.route('/area_json_by_name/<nombre>')
def area_json_byName(nombre):
    return a.area_json_byName(nombre)

#Defino la ruta para crear un contacto
@area.route('/area_add', methods=['POST'])
def area_create():
    return a.area_create()

#Defino la ruta para actualizar un contacto
@area.route('/area_update/<id>',methods=['POST'])
def area_update(id):
    return a.area_update(id)
#Defino la ruta para eliminar un contacto
@area.route('/area_delete/<id>')
def area_delete(id):
    return a.area_delete(id)