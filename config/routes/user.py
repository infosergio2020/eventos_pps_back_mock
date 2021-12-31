from flask import Blueprint, request, jsonify
from models.user import User #para añadir los datos a la tabla
user= Blueprint('user',__name__)
#Defino la ruta para mostrar la impresion
@user.route('/user')
def index():
    return jsonify(result = { 
        "listar_usuarios":"/users_json",
        "get_usuario_by_id":"/user_json_by_id/<id>",
        "get_usuario_by_email":"/user_json_by_email/<email>",
        "agregar usuario":"/user_add",
        "actualizar usuario":"/user_update/<id>",
        "borrar usuario":"/user_delete/<id>"
        })

#DEFINO LA RUTA PARA RETORNAR UN JSON CON TODOS LOS USUARIOS
@user.route('/users_json')
def users_json():
    """retorna un JSON que contiene un listado de usuarios"""
    result = User.all()
    return jsonify(user_list=[user.serialize for user in result])

@user.route('/user_json_by_id/<id>')
def user_json_byId(id):
    """retorna un JSON que contiene un usuario"""
    result = User.get_by_id(id)
    if result is not None:
        return jsonify(user = result.serialize)
    else:
        return jsonify(user = "nothing")

@user.route('/user_json_by_email/<email>')
def user_json_byEmail(email):
    """retorna un JSON que contiene un usuario"""
    result = User.find_by_email(email)
    if result is not None:
        return jsonify(user = result.serialize)
    else:
        return jsonify(user = "nothing")

#Defino la ruta para crear un contacto
@user.route('/user_add', methods=['POST'])
def user_create():
    try:
        data = request.get_json()
        User(
        data["name"],
        data["password"],
        data["email"]).save() #guardar los datos en la tabla
        return jsonify(result = "OK")
    except Exception:
        return jsonify(result = "error")

#Defino la ruta para actualizar un contacto
@user.route('/user_update/<id>',methods=['POST'])
def user_update(id):
        data = request.get_json()
        result = User.update(id,data["name"],data["password"],data["email"])
        if  result != None:
            return jsonify(result = result.serialize)
        # si es un GET o no se actualizo me voy al form para actualizar
        return jsonify(result = "nothing")

#Defino la ruta para eliminar un contacto
@user.route('/user_delete/<id>')
def user_delete(id):
    result = User.delete(id)
    if  result != None:
        return jsonify(result = result.serialize)
    return jsonify(result = "nothing")
