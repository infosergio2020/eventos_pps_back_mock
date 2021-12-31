from flask import request, jsonify
from models.evento import Evento #para añadir los datos a la tabla
from sqlalchemy import exc, Date, Time, cast

# /
def index():
    """da una descripcion de las rutas que se pueden usar para acceder a los servicios"""
    return jsonify(result = { 
        "listar_evento":"/evento/get-all",
        "get_evento_by_id":"/evento/get-by-id/<id>",
        "get_evento_by_email":"evento/get-by-name/<name>",
        "agregar_evento":"evento/add",
        "actualizar_evento":"evento/update/<id>",
        "borrar_evento":"evento/delete/<id>"
        })
# /get-all
def evento_json():
    """retorna un JSON que contiene un listado de usuarios"""
    result = Evento.all()
    return jsonify(evento_list=[evento.serialize for evento in result])
# /get-by-id/<id>
def evento_json_byId(id):
    """retorna un JSON que contiene un usuario"""
    result = Evento.get_by_id(id)
    if result is not None:
        return jsonify(user = result.serialize)
    else:
        return jsonify(user = "nothing")
# /get-by-name/<name>
def evento_json_byname(name):
    """retorna un JSON que contiene un usuario"""
    result = Evento.find_by_name(name)
    if result is not None:
        return jsonify(user = result.serialize)
    else:
        return jsonify(user = "nothing")
# /add        only evento
# el JSON de postman debe tener areas = [] o sino se rompe en la linea 53
def evento_create():
    try:
        data = request.get_json()
        
        evento_guardado = Evento(
        data["nombre"],
        data["lugar"],
        data["descripcion"],
        cast(data["fecha"],Date),
        cast(data["hora"],Time))

        evento_guardado.save()

        # solo si el formulario agregar areas 
        if len(data["areas"]) != 0:
            areas = data["areas"]
            for area in areas:
                evento_guardado.agregar_area(area['nombre'],area['descripcion'])
            
        return jsonify(result = "OK")
    except exc.SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        return jsonify(result = error)

# /update
def evento_update(id):
        data = request.get_json()
        result = Evento.update(id,
        data["nombre"],
        data["lugar"],
        data["descripcion"],
        cast(data["fecha"],Date),
        cast(data["hora"],Time))
        if  result != None:
            return jsonify(result = result.serialize)
        # si es un GET o no se actualizo me voy al form para actualizar
        return jsonify(result = "nothing")
# /delete
def evento_delete(id):
    result = Evento.delete(id)
    if  result != None:
        return jsonify(result = result.serialize)
    return jsonify(result = "nothing")