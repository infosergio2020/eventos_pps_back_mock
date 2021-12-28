from flask import Blueprint, render_template, request, redirect, url_for
from flask.helpers import flash
from models.user import User #para añadir los datos a la tabla
from utils.db import db #para guardarme la tabla en la base de datos


user= Blueprint('user',__name__)

#Defino la ruta para mostrar la impresion
@user.route('/')
def index():
    aux_users=User.query.all()
    return render_template('index.html',users=aux_users)

#Defino la ruta para crear un contacto
@user.route('/user', methods=['POST'])
def add_user():
    nom=request.form['name']
    password=request.form['pasword']
    email=request.form['email']
    new_user=User(nom,password,email) #agrego datos a la tabla user
    db.session.add(new_user) #agrego la tabla en la base de datos
    db.session.commit() # cierro la conexion con la base de datos
    flash("se añadio un usuario correctamente")
    return redirect('/')

#Defino la ruta para actualizar un contacto
@user.route('/update/<id>',methods=['POST','GET'])
def update(id):

    aux_user=User.query.get(id) #Busco al usuario en la tabla

    if(request.method=='POST'):
        aux_user.name=request.form['name']
        aux_user.password=request.form['pasword']
        aux_user.email=request.form['email']
        db.session.commit() # cierro la conexion con la base de datos
        flash("se actualizo un usuario correctamente")
        return redirect(url_for('user.index'))
    
    # flash("se añadio un usuario correctamente")
    return render_template('update.html',users=aux_user)

#Defino la ruta para eliminar un contacto
@user.route('/delete/<id>')
def delete(id):
    aux_user=User.query.get(id) #Busco al usuario en la tabla
    db.session.delete(aux_user) # eliminno desde la BD
    db.session.commit()
    flash("se elimino un usuario correctamente")
    return redirect(url_for('user.index')) #redirecciono a una funcion

