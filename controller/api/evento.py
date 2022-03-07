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
        
        if 'nombre' in data:
            if 'lugar' in data:
                if 'descripcion' in data:
                    if 'fecha' in data:
                        if 'hora' in data:
                            evento_guardado = Evento(
                            data["nombre"],
                            data["lugar"],
                            data["descripcion"],
                            cast(data["fecha"],Date),
                            cast(data["hora"],Time))
                            evento_guardado.save()
                            # solo si el formulario agregar areas 
                            if 'areas' in data:
                                areas = data["areas"]
                                for area in areas:
                                    evento_guardado.agregar_area(area['nombre'],area['descripcion'])                         
                            # solo si el formulario agregar areas 
                            if 'fotos' in data:
                                fotos = data["fotos"]
                                for foto in fotos:
                                    print(foto)
                                    evento_guardado.agregar_foto(foto['titulo'],foto['url'],foto['descripcion'])
                            # solo si el formulario agregar areas 
                            if 'videos' in data:
                                videos = data["videos"]
                                for video in videos:
                                    print(video)
                                    evento_guardado.agregar_video(video['titulo'],video['url'],video['descripcion'])    
                            return jsonify(result = "OK")
                        else:
                            return jsonify(result = {"res":"error","msj":'falta el campo hora'})
                    else:
                        return jsonify(result = {"res":"error","msj":'falta el campo fecha'})
                else:
                    return jsonify(result = {"res":"error","msj":'falta el campo descripcion'})
            else:
                return jsonify(result = {"res":"error","msj":'falta el campo lugar'})
        else:
            return jsonify(result = {"res":"error","msj":'falta el campo nombre'})

    except exc.SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        return jsonify(result = {"msj":"error SQLAlchemy","codigo":error})

# /update
def evento_update(id):
        data = request.get_json()
        result = Evento.update(id,
        data["nombre"],
        data["lugar"],
        data["descripcion"],
        cast(data["fecha"],Date),
        cast(data["hora"],Time))
        
        #si se agregar mas areas como actualizacion... 
        evento_actualizado = Evento.get_by_id(id)
        # solo si el formulario agregar areas 
        if 'areas' in data:
            areas = data["areas"]
            for area in areas:
                evento_actualizado.agregar_area(area['nombre'],area['descripcion'])                         
        # solo si el formulario agregar areas 
        if 'fotos' in data:
            fotos = data["fotos"]
            for foto in fotos:
                print(foto)
                evento_actualizado.agregar_foto(foto['titulo'],foto['url'],foto['descripcion'])
        # solo si el formulario agregar areas 
        if 'videos' in data:
            videos = data["videos"]
            for video in videos:
                print(video)
                evento_actualizado.agregar_video(video['titulo'],video['url'],video['descripcion'])    


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