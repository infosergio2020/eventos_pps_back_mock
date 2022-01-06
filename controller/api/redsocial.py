from flask import request, jsonify
from models.redsocial import Redsocial

#Defino la ruta para mostrar la impresion
def index():
    return jsonify(result = { 
        "listar_redsocial":"/redsocial_json",
        "get_redsocial_by_id":"/redsocial_json_by_id/<id>",
        "get_redsocial_by_email":"/redsocial_json_by_name/<name>",
        "agregar_redsocial":"/redsocial_add",
        "actualizar_redsocial":"/redsocial_update/<id>",
        "borrar_redsocial":"/redsocial_delete/<id>"
        })

#DEFINO LA RUTA PARA RETORNAR UN JSON CON TODOS LOS USUARIOS
def redsocial_json():
    """retorna un JSON que contiene un listado de usuarios"""
    result = Redsocial.all()
    return jsonify(redsocial_list=[redsocial.serialize for redsocial in result])

def redsocial_json_byId(id):
    """retorna un JSON que contiene un usuario"""
    result = Redsocial.get_by_id(id)
    if result is not None:
        return jsonify(redsocial = result.serialize)
    else:
        return jsonify(redsocial = "nothing")

def redsocial_json_byname(name):
    """retorna un JSON que contiene un usuario"""
    result = Redsocial.find_by_name(name)
    if result is not None:
        return jsonify(redsocial = result.serialize)
    else:
        return jsonify(redsocial = "nothing")

#Defino la ruta para crear un contacto
def redsocial_create():
    try:
        data = request.get_json()
        Redsocial(data["nombre"]).save() #guardar los datos en la tabla
        return jsonify(result = "OK")
    except Exception:
        return jsonify(result = "error")

#Defino la ruta para actualizar un contacto
def redsocial_update(id):
        data = request.get_json()
        result = Redsocial.update(id,
        data["nombre"])
        if  result != None:
            return jsonify(result = result.serialize)
        # si es un GET o no se actualizo me voy al form para actualizar
        return jsonify(result = "nothing")

#Defino la ruta para eliminar un contacto
def redsocial_delete(id):
    result = Redsocial.delete(id)
    if  result != None:
        return jsonify(result = result.serialize)
    return jsonify(result = "nothing")
