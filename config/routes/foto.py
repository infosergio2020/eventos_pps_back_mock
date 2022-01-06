from controller.api import foto as f
from flask import Blueprint
foto= Blueprint('foto',__name__)

#Defino la ruta para mostrar la impresion
@foto.route('/')
def index():
    return f.index()

#DEFINO LA RUTA PARA RETORNAR UN JSON CON TODOS LOS USUARIOS
@foto.route('/foto_json')
def foto_json():
    return f.foto_json()

@foto.route('/foto_json_by_id/<id>')
def foto_json_byId(id):
    return f.foto_json_byId(id)

@foto.route('/foto_json_by_title/<title>')
def foto_json_bytitle(title):
    return f.foto_json_bytitle(title)

#Defino la ruta para crear un contacto
@foto.route('/foto_add', methods=['POST'])
def foto_create():
    return f.foto_create()

#Defino la ruta para actualizar un contacto
@foto.route('/foto_update/<id>',methods=['POST'])
def foto_update(id):
    return f.foto_update(id)
    
#Defino la ruta para eliminar un contacto
@foto.route('/foto_delete/<id>')
def foto_delete(id):
    return f.foto_delete(id)
