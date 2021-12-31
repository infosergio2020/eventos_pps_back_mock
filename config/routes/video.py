from flask import Blueprint, request, jsonify
from models.video import Video #para añadir los datos a la tabla
video= Blueprint('video',__name__)

#Defino la ruta para mostrar la impresion
@video.route('/')
def index():
    return jsonify(result = { 
        "listar_video":"/video_json",
        "get_video_by_id":"/video_json_by_id/<id>",
        "get_video_by_email":"/video_json_by_name/<name>",
        "agregar_video":"/video_add",
        "actualizar_video":"/video_update/<id>",
        "borrar_video":"/video_delete/<id>"
        })

#DEFINO LA RUTA PARA RETORNAR UN JSON CON TODOS LOS USUARIOS
@video.route('/video_json')
def video_json():
    """retorna un JSON que contiene un listado de usuarios"""
    result = Video.all()
    return jsonify(video_list=[video.serialize for video in result])

@video.route('/video_json_by_id/<id>')
def video_json_byId(id):
    """retorna un JSON que contiene un usuario"""
    result = Video.get_by_id(id)
    if result is not None:
        return jsonify(video = result.serialize)
    else:
        return jsonify(video = "nothing")

@video.route('/video_json_by_title/<title>')
def video_json_byTitle(title):
    """retorna un JSON que contiene un usuario"""
    result = Video.find_by_titulo(title)
    if result is not None:
        return jsonify(video = result.serialize)
    else:
        return jsonify(video = "nothing")

#Defino la ruta para crear un contacto
@video.route('/video_add', methods=['POST'])
def video_create():
    try:
        data = request.get_json()
        Video( data["titulo"],
              data["url"],
              data["descripcion"]).save() #guardar los datos en la tabla
        return jsonify(result = "OK")
    except Exception:
        return jsonify(result = "error")

#Defino la ruta para actualizar un contacto
@video.route('/video_update/<id>',methods=['POST'])
def foto_update(id):
        data = request.get_json()
        result = Video.update(id,
            data["titulo"],
            data["url"],
            data["descripcion"])
        if  result != None:
            return jsonify(result = result.serialize)
        # si es un GET o no se actualizo me voy al form para actualizar
        return jsonify(result = "nothing")

#Defino la ruta para eliminar un contacto
@video.route('/video_delete/<id>')
def video_delete(id):
    result = Video.delete(id)
    if  result != None:
        return jsonify(result = result.serialize)
    return jsonify(result = "nothing")
