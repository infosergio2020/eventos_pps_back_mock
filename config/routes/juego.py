from flask import Blueprint, request, jsonify
from models.juego import Juego #para añadir los datos a la tabla
juego = Blueprint('juego',__name__)
#Defino la ruta para mostrar la impresion
@juego.route('/')
def index():
    return jsonify(result = { 
        "listar_juegos":"/juego_json",
        "get_juego_by_id":"/juego_json_by_id/<id>",
        "get_juego_by_email":"/juego_json_by_name/<name>",
        "agregar_juego":"/juego_add",
        "actualizar_juego":"/juego_update/<id>",
        "borrar_juego":"/juego_delete/<id>"
        })

#DEFINO LA RUTA PARA RETORNAR UN JSON CON TODOS LOS USUARIOS
@juego.route('/juego_json')
def juego_json():
    """retorna un JSON que contiene un listado de usuarios"""
    result = Juego.all()
    return jsonify(juego_list=[juego.serialize for juego in result])

@juego.route('/juego_json_by_id/<id>')
def juego_json_byId(id):
    """retorna un JSON que contiene un usuario"""
    result = Juego.get_by_id(id)
    if result is not None:
        return jsonify(juego = result.serialize)
    else:
        return jsonify(juego = "nothing")

@juego.route('/juego_json_by_name/<name>')
def juego_json_byname(name):
    """retorna un JSON que contiene un usuario"""
    result = Juego.find_by_name(name)
    if result is not None:
        return jsonify(juego = result.serialize)
    else:
        return jsonify(juego = "nothing")

#Defino la ruta para crear un contacto
@juego.route('/juego_add', methods=['POST'])
def juego_create():
    try:
        data = request.get_json()
        Juego(
        data["nombre"],
        data["url_juego"],
        data["url_imagen"],
        data["descripcion"]).save() #guardar los datos en la tabla
        return jsonify(result = "OK")
    except Exception:
        return jsonify(result = "error")

#Defino la ruta para actualizar un contacto
@juego.route('/juego_update/<id>',methods=['POST'])
def juego_update(id):
        data = request.get_json()
        result = Juego.update(id,
        data["nombre"],
        data["url_juego"],
        data["url_imagen"],
        data["descripcion"])
        if  result != None:
            return jsonify(result = result.serialize)
        # si es un GET o no se actualizo me voy al form para actualizar
        return jsonify(result = "nothing")

#Defino la ruta para eliminar un contacto
@juego.route('/juego_delete/<id>')
def juego_delete(id):
    result = Juego.delete(id)
    if  result != None:
        return jsonify(result = result.serialize)
    return jsonify(result = "nothing")
