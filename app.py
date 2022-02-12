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


@app.route('/Conclusiones-del-evento.html')
def Conclusionesdelevento():
    
    return render_template('/Conclusiones-del-evento.html')   

@app.route('/diarios.html')
def Diarios():
    
    return render_template('/diarios.html')   

@app.route('/Inundaciones-en-el-exterior.html')
def Inundacionesenelexterior():
    
    return render_template('/Inundaciones-en-el-exterior.html')     

@app.route('/photo-album.html')
def Photoalbum():
    
    return render_template('/photo-album.html')   

######################
# carpeta sections
#####################                       
@app.route('/sections/section-1.html')
def Section1():  
    return render_template('/sections/section-1.html')   

@app.route('/sections/section-2.html')
def Section2():  
    return render_template('/sections/section-2.html')   

@app.route('/sections/section-3.html')
def Section3():  
    return render_template('/sections/section-3.html')   

@app.route('/sections/section-4.html')
def Section4():  
    return render_template('/sections/section-4.html')  

@app.route('/sections/section-5.html')
def Section5():  
    return render_template('/sections/section-5.html')   

@app.route('/sections/section-6.html')
def Section6():  
    return render_template('/sections/section-6.html')  


######################
# carpeta menu-deslizante
#####################                       
@app.route('/about.html')
def About():  
    return render_template('/about.html')   

@app.route('/anounce.html')
def Anounce():  
    return render_template('/anounce.html')   

@app.route('/covid.html')
def Covid():  
    return render_template('/covid.html')   

@app.route('/languaje.html')
def Languaje():  
    return render_template('/languaje.html')  

@app.route('/menu-deslizante/sections.html')
def Sections():  
    return render_template('/menu-deslizante/sections.html')  



######################
# carpeta inundacion-exterior
#####################                       
@app.route('/inundacion-exterior/alemania.html')
def Alemania():  
    return render_template('/inundacion-exterior/alemania.html')   

@app.route('/inundacion-exterior/chile.html')
def Chile():  
    return render_template('/inundacion-exterior/chile.html')   

@app.route('/inundacion-exterior/polonia.html')
def Polonia():  
    return render_template('/inundacion-exterior/polonia.html')  


######################
# carpeta conclusion del evento
#####################                       
@app.route('/conclusion-del-evento/la-ayuda-de-la-radio.html')
def Radio():  
    return render_template('/conclusion-del-evento/la-ayuda-de-la-radio.html')   

@app.route('/conclusion-del-evento/la-importancia-de-la-solidaridad.html')
def Soliradidad():  
    return render_template('/conclusion-del-evento/la-importancia-de-la-solidaridad.html')   

@app.route('/conclusion-del-evento/legado-memoria.html')
def Legadomemoria():  
    return render_template('/conclusion-del-evento/legado-memoria.html')   

@app.route('/conclusion-del-evento/reflexiones-de-los-entrevistados.html')
def Reflexiones():  
    return render_template('/conclusion-del-evento/reflexiones-de-los-entrevistados.html')                                    
# app.secret_key="secret key" # configuro un valor para que se genere una sesion
# 
# SQLAlchemy(app) #le paso al ORM la configuracion que posee el app  #Configuracion del app
# app.register_blueprint(user) #invoco las rutas del usuario
# app.register_blueprint(evento)
    
