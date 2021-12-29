from flask import Blueprint, request, jsonify
from models.evento import Evento #para añadir los datos a la tabla
evento= Blueprint('evento',__name__)
#Defino la ruta para mostrar la impresion
@evento.route('/')
def index():
    return jsonify(result = { 
        "listar_evento":"/evento_json",
        "get_evento_by_id":"/evento_json_by_id/<id>",
        "get_evento_by_email":"/evento_json_by_name/<name>",
        "agregar_evento":"/evento_add",
        "actualizar_evento":"/evento_update/<id>",
        "borrar_evento":"/evento_delete/<id>"
        })

#DEFINO LA RUTA PARA RETORNAR UN JSON CON TODOS LOS USUARIOS
@evento.route('/evento_json')
def evento_json():
    """retorna un JSON que contiene un listado de usuarios"""
    result = Evento.all()
    return jsonify(evento_list=[evento.serialize for evento in result])

@evento.route('/user_json_by_id/<id>')
def user_json_byId(id):
    """retorna un JSON que contiene un usuario"""
    result = Evento.get_by_id(id)
    if result is not None:
        return jsonify(user = result.serialize)
    else:
        return jsonify(user = "nothing")

@evento.route('/user_json_by_name/<name>')
def user_json_byname(name):
    """retorna un JSON que contiene un usuario"""
    result = Evento.find_by_name(name)
    if result is not None:
        return jsonify(user = result.serialize)
    else:
        return jsonify(user = "nothing")

#Defino la ruta para crear un contacto
@evento.route('/evento_add', methods=['POST'])
def evento_create():
    try:
        data = request.get_json()
        Evento(
        data["nombre"],
        data["lugar"],
        data["descripcion"],
        data["fecha"],
        data["hora"]).save() #guardar los datos en la tabla
        return jsonify(result = "OK")
    except Exception:
        return jsonify(result = "error")

#Defino la ruta para actualizar un contacto
@evento.route('/evento_update/<id>',methods=['POST'])
def evento_update(id):
        data = request.get_json()
        result = Evento.update(id,
        data["nombre"],
        data["lugar"],
        data["descripcion"],
        data["fecha"],
        data["hora"])
        if  result != None:
            return jsonify(result = result.serialize)
        # si es un GET o no se actualizo me voy al form para actualizar
        return jsonify(result = "nothing")

#Defino la ruta para eliminar un contacto
@evento.route('/evento_delete/<id>')
def evento_delete(id):
    result = Evento.delete(id)
    if  result != None:
        return jsonify(result = result.serialize)
    return jsonify(result = "nothing")
