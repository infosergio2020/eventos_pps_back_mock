from flask import Blueprint
from controller.api import envivo as en
envivo = Blueprint('envivo',__name__)
#Defino la ruta para mostrar la impresion
@envivo.route('/')
def index():
    return en.index()
#DEFINO LA RUTA PARA RETORNAR UN JSON CON TODOS LOS USUARIOS
@envivo.route('/envivo_json')
def envivo_json():
    return en.envivo_json()
@envivo.route('/envivo_json_by_id/<id>')
def envivo_json_byId(id):
    return en.envivo_json_byId(id)
@envivo.route('/envivo_json_by_name/<name>')
def envivo_json_byname(name):
    return en.envivo_json_byname(name)
#Defino la ruta para crear un contacto
@envivo.route('/envivo_add', methods=['POST'])
def envivo_create():
    return en.envivo_create()
#Defino la ruta para actualizar un contacto
@envivo.route('/juego_update/<id>',methods=['POST'])
def envivo_update(id):
    return en.envivo_update(id)
#Defino la ruta para eliminar un contacto
@envivo.route('/envivo_delete/<id>')
def envivo_delete(id):
    return en.envivo_delete(id)