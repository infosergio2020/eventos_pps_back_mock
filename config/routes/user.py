from controller.api import user as u
from flask import Blueprint
user= Blueprint('user',__name__)
#Defino la ruta para mostrar la impresion
@user.route('/user')
def index():
    return u.index()

#DEFINO LA RUTA PARA RETORNAR UN JSON CON TODOS LOS USUARIOS
@user.route('/users_json')
def users_json():
    return u.users_json()

@user.route('/user_json_by_id/<id>')
def user_json_byId(id):
    return u.user_json_byId(id)

@user.route('/user_json_by_email/<email>')
def user_json_byEmail(email):
    return u,user_json_byEmail(email)

#Defino la ruta para crear un contacto
@user.route('/user_add', methods=['POST'])
def user_create():
    return u.user_create()

#Defino la ruta para actualizar un contacto
@user.route('/user_update/<id>',methods=['POST'])
def user_update(id):
    return u.user_update(id)

#Defino la ruta para eliminar un contacto
@user.route('/user_delete/<id>')
def user_delete(id):
    return u.user_delete(id)