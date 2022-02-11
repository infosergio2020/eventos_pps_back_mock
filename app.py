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
    # return render_template('index.html')
    return rutas.render_index()
