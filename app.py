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

@app.route('/testimonio1')
def Testimonio1():
    
    return render_template('/testimonio1.html')    

@app.route('/testimonio2.html')
def Testimonio2():
    
    return render_template('/testimonio2.html')  


@app.route('/testimonio3.html')
def Testimonio3():
    
    return render_template('/testimonio3.html')   

@app.route('/water-level-simulator.html')
def Waterlevelsimulator():
    
    return render_template('/water-level-simulator.html')   


@app.route('/the-news-of-the-day.html')
def Thenewsoftheday():
    
    return render_template('/the-news-of-the-day.html')   


@app.route('/Why-do-we-flood.html')
def Whydoweflood():
    
    return render_template('/Why-do-we-flood.html')         

@app.route('/recomendacion-como-actuar.html')
def Recomendacioncomoactuar():
    
    return render_template('/recomendacion-como-actuar.html')         


@app.route('/sandbox.html')
def Sandbox():
    
    return render_template('/sandbox.html')         


@app.route('/shocking-photos.html')
def Shockingphotos():
    
    return render_template('/shocking-photos.html')         

# app.secret_key="secret key" # configuro un valor para que se genere una sesion
# 
# SQLAlchemy(app) #le paso al ORM la configuracion que posee el app  #Configuracion del app
# app.register_blueprint(user) #invoco las rutas del usuario
# app.register_blueprint(evento)
    
