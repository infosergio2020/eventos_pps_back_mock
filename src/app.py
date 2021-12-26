# comienzo
from flask import Flask
##Configuracion del app
app= Flask(__name__)

#Defino la ruta para crear el user
@app.route('/')
def home():
    return 'received'
    
# # inicia app
if __name__=='__main__':
    app.run(debug=True)



# , request
# from flask_sqlalchemy import SQLAlchemy
# from flask_marshmallow import Marshmallow
# from werkzeug.exceptions import MethodNotAllowed

# #Configuracion del app
# app= Flask(__name__)
# app.config['SQL_ALCHEMY_DATABASE_URI']='mysql://root:admin123@localhost/eventos'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
# #Configuracion del app

# db=SQLAlchemy(app) #le paso al ORM la configuracion que posee el app
# ma=Marshmallow(app) #instanciar un esquema

# class User(db.Model):
#     iduser= db.Column(db.Integer, primary_key=True)
#     name= db.Column(db.String(45))
#     password= db.Column(db.String(125))
#     email= db.Column(db.String(125), unique=True)

#     def __init__(self,name,password,email):
#         self.name=name
#         self.password=password
#         self.email=email

# db.create_all() #crea las tablas

# #esquema para interactuar
# class UserSchema(ma.Schema):
#     class Meta:
#         fields=('id','name','password','email')
# user_schema= UserSchema() #esquema user instanciado
# users_schema= UserSchema(many=True) #esquema devarios usuarios instanciadps

# #Defino la ruta para crear el user
# @app.route('/users',methods=['POST'])
# def create_user():
#     print(request.json)
#     return 'received'



