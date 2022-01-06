from flask import request, jsonify
from models.user import User #para añadir los datos a la tabla

def index():
    return jsonify(result = { 
        "listar_usuarios":"/users_json",
        "get_usuario_by_id":"/user_json_by_id/<id>",
        "get_usuario_by_email":"/user_json_by_email/<email>",
        "agregar usuario":"/user_add",
        "actualizar usuario":"/user_update/<id>",
        "borrar usuario":"/user_delete/<id>"
        })

def users_json():
    """retorna un JSON que contiene un listado de usuarios"""
    result = User.all()
    return jsonify(user_list=[user.serialize for user in result])

def user_json_byId(id):
    """retorna un JSON que contiene un usuario"""
    result = User.get_by_id(id)
    if result is not None:
        return jsonify(user = result.serialize)
    else:
        return jsonify(user = "nothing")

def user_json_byEmail(email):
    """retorna un JSON que contiene un usuario"""
    result = User.find_by_email(email)
    if result is not None:
        return jsonify(user = result.serialize)
    else:
        return jsonify(user = "nothing")

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

def user_update(id):
        data = request.get_json()
        result = User.update(id,data["name"],data["password"],data["email"])
        if  result != None:
            return jsonify(result = result.serialize)
        # si es un GET o no se actualizo me voy al form para actualizar
        return jsonify(result = "nothing")

def user_delete(id):
    result = User.delete(id)
    if  result != None:
        return jsonify(result = result.serialize)
    return jsonify(result = "nothing")