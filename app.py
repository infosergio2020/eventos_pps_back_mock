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
    return rutas.render_index()

@app.route('/testimonio1')
def Testimonio1():
    return rutas.render_before_flood()

@app.route('/testimonio2')
def Testimonio2():
    return rutas.render_during_flood()

@app.route('/testimonio3')
def Testimonio3():
    return rutas.render_after_flood()


@app.route('/water-level-simulator')
def Waterlevelsimulator():
    return rutas.render_agua_simulador()

@app.route('/the-news-of-the-day')
def Thenewsoftheday():
    return rutas.render_noticias_dia()

@app.route('/Why-do-we-flood')
def Whydoweflood():
    return rutas.render_why_do_we_flood()

@app.route('/recomendacion-como-actuar')
def Recomendacioncomoactuar():
    return rutas.render_recomendacion()


@app.route('/sandbox')
def Sandbox():
    return rutas.render_sandbox()


@app.route('/shocking-photos')
def Shockingphotos():
    return rutas.render_shocking_photos()


@app.route('/Conclusiones-del-evento')
def Conclusionesdelevento():
    return rutas.render_conclusiones()

@app.route('/diarios')
def Diarios():
    return rutas.render_diarios()

@app.route('/Inundaciones-en-el-exterior')
def Inundacionesenelexterior():
    return rutas.render_inundacion_exterior()

@app.route('/photo-album')
def Photoalbum():
    return rutas.render_photo_album()

######################
# carpeta sections
#####################                       
@app.route('/sections/section-1')
def Section1():  
    return rutas.render_section_1()

@app.route('/sections/section-2')
def Section2():  
    return rutas.render_section_2()

@app.route('/sections/section-3')
def Section3():  
    return rutas.render_section_3()

@app.route('/sections/section-4')
def Section4():  
    return rutas.render_section_4()

@app.route('/sections/section-5')
def Section5():  
    return rutas.render_section_5()

@app.route('/sections/section-6')
def Section6():  
    return rutas.render_section_6()


######################
# carpeta menu-deslizante
#####################                       
@app.route('/about')
def About():  
    return rutas.render_about()

@app.route('/anounce')
def Anounce():  
    return rutas.render_announcements()

@app.route('/covid')
def Covid():  
    return rutas.render_covid()

@app.route('/languaje')
def Languaje():  
    return rutas.render_languaje()

@app.route('/sections')
def Sections():  
    return rutas.render_sections()



######################
# carpeta inundacion-exterior
#####################

@app.route('/inundacion-exterior')
def inundacion_exterior():  
    return rutas.render_inundacion_exterior()

@app.route('/inundacion-exterior/alemania')
def alemania():  
    return rutas.render_alemania()

@app.route('/inundacion-exterior/chile')
def chile():  
    return rutas.render_chile()

@app.route('/inundacion-exterior/polonia')
def polonia():  
    return rutas.render_polonia()


######################
# carpeta conclusion del evento
#####################       

@app.route('/conclusion-del-evento')
def conclusion():  
    return rutas.render_conclusiones()

@app.route('/conclusion-del-evento/la-ayuda-de-la-radio')
def Radio():  
    return rutas.render_conclusiones_radio()

@app.route('/conclusion-del-evento/la-importancia-de-la-solidaridad')
def Soliradidad():  
    return rutas.render_conclusiones_solidaridad()

@app.route('/conclusion-del-evento/legado-memoria')
def Legadomemoria():  
    return rutas.render_conclusiones_legado_memoria()

@app.route('/conclusion-del-evento/reflexiones-de-los-entrevistados')
def Reflexiones():  
    return rutas.render_conclusiones_reflexiones()
