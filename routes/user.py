from flask import Blueprint, render_template, request
from models.user import user #para añadir los datos a la tabla
from utils.db import db #para guardarme la tabla en la base de datos


user= Blueprint('user',__name__)

#Defino la ruta para mostrar la impresion
@user.route('/')
def home():
    return render_template('index.html')

#Defino la ruta para crear un contacto
@user.route('/user', methods=['POST'])
def add_user():
    nom=request.form['name']
    password=request.form['pasword']
    email=request.form['email']
    new_user=user(nom,password,email) #agrego datos a la tabla user
    db.session.add(new_user) #agrego la tabla en la base de datos
    db.session.commit() # cierro la conexion con la base de datos
    return "usuario guardado"

#Defino la ruta para actualizar un contacto
@user.route('/update')
def update_user():
    return 'update usuario'

#Defino la ruta para eliminar un contacto
@user.route('/delete')
def delete_user():
    return 'delete usuario'

