# comienzo
from flask import Flask,render_template
from entorno import config
from modules.rederizado import CustomRouter

rutas = CustomRouter()

##Configuracion del app
app = Flask(__name__)
app.config.from_object(config)

#colocar las rutas antes de correr el servidor
@app.route('/')
def Index():
    
    return render_template('index.html')

@app.route('/testimonio1.html')
def Testimonio1():
    
    return render_template('/testimonio1.html')    
# app.secret_key="secret key" # configuro un valor para que se genere una sesion
# 
# SQLAlchemy(app) #le paso al ORM la configuracion que posee el app  #Configuracion del app
# app.register_blueprint(user) #invoco las rutas del usuario
# app.register_blueprint(evento)
    
