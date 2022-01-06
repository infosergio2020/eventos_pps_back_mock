from controller.api import juego as j
from flask import Blueprint
juego = Blueprint('juego',__name__)
#Defino la ruta para mostrar la impresion
@juego.route('/')
def index():
    return j.index()

#DEFINO LA RUTA PARA RETORNAR UN JSON CON TODOS LOS USUARIOS
@juego.route('/juego_json')
def juego_json():
   return j.juego_json()

@juego.route('/juego_json_by_id/<id>')
def juego_json_byId(id):
    return j.juego_json_byId(id)

@juego.route('/juego_json_by_name/<name>')
def juego_json_byname(name):
   return j.juego_json_byname(name)

#Defino la ruta para crear un contacto
@juego.route('/juego_add', methods=['POST'])
def juego_create():
    return j.juego_create()

#Defino la ruta para actualizar un contacto
@juego.route('/juego_update/<id>',methods=['POST'])
def juego_update(id):
    return j.juego_update(id)

#Defino la ruta para eliminar un contacto
@juego.route('/juego_delete/<id>')
def juego_delete(id):
   return j.juego_delete(id)