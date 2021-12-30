from flask import Blueprint, render_template, request, redirect, url_for
from flask.helpers import flash
from models.area import Area #para añadir los datos a la tabla
from utils.db import db #para guardarme la tabla en la base de datos


area= Blueprint('area',__name__)

#Defino la ruta para mostrar la impresion
@area.route('/crearArea')
def index_area():
    aux_areas=Area.query.all()
    return render_template('area.html',areas=aux_areas)

#Defino la ruta para crear un contacto
@area.route('/area', methods=['POST'])
def add_area():
    nom=request.form['name']
    # password=request.form['pasword']
    # email=request.form['email']
    new_area=Area(nom) #agrego datos a la tabla area
    db.session.add(new_area) #agrego la tabla en la base de datos
    db.session.commit() # cierro la conexion con la base de datos
    flash("se añadio un area correctamente")
    return redirect('/crearArea')

#Defino la ruta para actualizar un contacto
@area.route('/update_area/<id>',methods=['POST','GET'])
def update(id):

    aux_area=Area.query.get(id) #Busco al area en la tabla

    if(request.method=='POST'):
        aux_area.name=request.form['name']
        # aux_area.password=request.form['pasword']
        # aux_area.email=request.form['email']
        db.session.commit() # cierro la conexion con la base de datos
        flash("se actualizo un area correctamente")
        return redirect(url_for('area.index_area'))
    
    # flash("se añadio un area correctamente")
    return render_template('area_update.html',areas=aux_area)

#Defino la ruta para eliminar un contacto
@area.route('/delete_area/<id>')
def delete(id):
    aux_area=Area.query.get(id) #Busco al area en la tabla
    db.session.delete(aux_area) # eliminno desde la BD
    db.session.commit()
    flash("se elimino un area correctamente")
    return redirect(url_for('area.index_area')) #redirecciono a una funcion

