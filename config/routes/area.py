from flask import Blueprint, request, jsonify
from models.area import Area #para añadir los datos a la tabla
area= Blueprint('area',__name__)

#Defino la ruta para mostrar la impresion
@area.route('/')
def index():
    return jsonify(result = { 
        "listar_areas":"/area_json",
        "get_area_by_id":"/area_json_by_id/<id>",
        "get_area_by_email":"/area_json_by_name/<name>",
        "agregar_area":"/area_add",
        "actualizar_area":"/area_update/<id>",
        "borrar_area":"/area_delete/<id>"
        })

#DEFINO LA RUTA PARA RETORNAR UN JSON CON TODOS LOS USUARIOS
@area.route('/area_json')
def area_json():
    """retorna un JSON que contiene un listado de usuarios"""
    result = Area.all()
    return jsonify(area_list=[area.serialize for area in result])

@area.route('/area_json_by_id/<id>')
def area_json_byId(id):
    """retorna un JSON que contiene un usuario"""
    result = Area.get_by_id(id)
    if result is not None:
        return jsonify(area = result.serialize)
    else:
        return jsonify(area = "nothing")

@area.route('/area_json_by_name/<nombre>')
def area_json_byName(nombre):
    """retorna un JSON que contiene un usuario"""
    result = Area.find_by_name(nombre)
    if result is not None:
        return jsonify(area = result.serialize)
    else:
        return jsonify(area = "nothing")

#Defino la ruta para crear un contacto
@area.route('/area_add', methods=['POST'])
def area_create():
    try:
        data = request.get_json()
        Area( data["nombre"],
              data["descripcion"]).save() #guardar los datos en la tabla
        return jsonify(result = "OK")
    except Exception:
        return jsonify(result = "error")

#Defino la ruta para actualizar un contacto
@area.route('/area_update/<id>',methods=['POST'])
def area_update(id):
        data = request.get_json()
        result = Area.update(id,
            data["nombre"],
            data["descripcion"])
        if  result != None:
            return jsonify(result = result.serialize)
        # si es un GET o no se actualizo me voy al form para actualizar
        return jsonify(result = "nothing")

#Defino la ruta para eliminar un contacto
@area.route('/area_delete/<id>')
def area_delete(id):
    result = Area.delete(id)
    if  result != None:
        return jsonify(result = result.serialize)
    return jsonify(result = "nothing")
