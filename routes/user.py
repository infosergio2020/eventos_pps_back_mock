from flask import Blueprint, render_template, request, redirect, url_for
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
    return redirect('/')

#Defino la ruta para actualizar un contacto
@user.route('/update')
def update():
    return 'update usuario'

#Defino la ruta para eliminar un contacto
@user.route('/delete/<iduser>')
def delete(iduser):
    aux_user=User.query.get(iduser) #Busco al usuario en la tabla
    db.session.delete(aux_user) # eliminno desde la BD
    db.session.commit()
    return redirect(url_for('user.index')) #redirecciono a una funcion

