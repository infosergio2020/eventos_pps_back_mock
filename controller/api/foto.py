from flask import  request, jsonify
from models.foto import Foto #para añadir los datos a la tabla

def index():
    return jsonify(result = { 
        "listar_fotos":"/foto_json",
        "get_foto_by_id":"/foto_json_by_id/<id>",
        "get_foto_by_email":"/foto_json_by_name/<name>",
        "agregar_foto":"/foto_add",
        "actualizar_foto":"/foto_update/<id>",
        "borrar_foto":"/foto_delete/<id>"
        })

def foto_json():
    """retorna un JSON que contiene un listado de usuarios"""
    result = Foto.all()
    return jsonify(foto_list=[foto.serialize for foto in result])

def foto_json_byId(id):
    """retorna un JSON que contiene un usuario"""
    result = Foto.get_by_id(id)
    if result is not None:
        return jsonify(foto = result.serialize)
    else:
        return jsonify(foto = "nothing")

def foto_json_bytitle(title):
    """retorna un JSON que contiene un usuario"""
    result = Foto.find_by_titulo(title)
    if result is not None:
        return jsonify(foto = result.serialize)
    else:
        return jsonify(foto = "nothing")

def foto_create():
    try:
        data = request.get_json()
        Foto( data["titulo"],
              data["url"],
              data["descripcion"]).save() #guardar los datos en la tabla
        return jsonify(result = "OK")
    except Exception:
        return jsonify(result = "error")

def foto_update(id):
        data = request.get_json()
        result = Foto.update(id,
            data["titulo"],
            data["url"],
            data["descripcion"])
        if  result != None:
            return jsonify(result = result.serialize)
        # si es un GET o no se actualizo me voy al form para actualizar
        return jsonify(result = "nothing")

def foto_delete(id):
    result = Foto.delete(id)
    if  result != None:
        return jsonify(result = result.serialize)
    return jsonify(result = "nothing")