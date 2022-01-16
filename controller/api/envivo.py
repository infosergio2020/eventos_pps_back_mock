from flask import  request, jsonify
from models.envivo import Envivo #para añadir los datos a la tabla

def index():
    return jsonify(result = { 
        "listar_envivos":"/envivo_json",
        "get_envivo_by_id":"/envivo_json_by_id/<id>",
        "get_envivo_by_email":"/envivo_json_by_name/<name>",
        "agregar_envivo":"/envivo_add",
        "actualizar_envivo":"/envivo_update/<id>",
        "borrar_envivo":"/envivo_delete/<id>"
        })

def envivo_json():
    """retorna un JSON que contiene un listado de usuarios"""
    result = Envivo.all()
    return jsonify(envivo_list=[envivo.serialize for envivo in result])

def envivo_json_byId(id):
    """retorna un JSON que contiene un usuario"""
    result = Envivo.get_by_id(id)
    if result is not None:
        return jsonify(envivo = result.serialize)
    else:
        return jsonify(envivo = "nothing")

def envivo_json_byname(name):
    """retorna un JSON que contiene un usuario"""
    result = Envivo.find_by_name(name)
    if result is not None:
        return jsonify(envivo = result.serialize)
    else:
        return jsonify(envivo = "nothing")




def envivo_create():
    try:
        data = request.get_json()
        Envivo(
            nomenvivo = data["nombre"],
            urlenvivo = data["url"],
            descenvivo = data["descripcion"],
            fechaenvivo = data["fecha"],
            horaenvivo = data["hora"]).save() #guardar los datos en la tabla
        return jsonify(result = "OK")
    except Exception:
        return jsonify(result = "error")

def envivo_update(id):
        data = request.get_json()
        if(data != None):
            result = Envivo.update(id,
                nomenvivo = data["nombre"],
                urlenvivo = data["url"],
                descenvivo = data["descripcion"],
                fechaenvivo = data["fecha"],
                horaenvivo = data["hora"])
            if  result != None:
                return jsonify(result = result.serialize)
        # si es un GET o no se actualizo me voy al form para actualizar
        return jsonify(result = "nothing")

def envivo_delete(id):
    result = Envivo.delete(id)
    if  result != None:
        return jsonify(result = result.serialize)
    return jsonify(result = "nothing")
