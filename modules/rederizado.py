from flask import render_template,request
from .mock_data import list_album,list_shocking

class CustomRouter:

    # index
    def render_index(self):
        return render_template('index.html',flag_1="index",flag_2=" ")

    # secciones del sidebar
    def render_sections(self):
        return render_template('sidebar/sections.html')

    def render_announcements(self):
        return render_template('sidebar/anounce.html')

    def render_objetivo(self):
        return render_template('sidebar/objetivo.html')

    def render_recorrido(self):
        return render_template('sidebar/recorrido.html')

    def render_covid(self):
        return render_template('sidebar/covid.html')

    def render_about(self):
        return render_template('sidebar/about.html')

    def render_languaje(self):
        return render_template('sidebar/languaje.html')


    # secciones

    # seccion-1
    def render_section_1(self):
        return render_template('sections/section-1.html')

    # subseccion-1
    def render_before_flood(self):
        return render_template('/testimonio1.html',flag_1="opcion_4",flag_2="opcion_3")

    def render_noticias_dia(self):
        return render_template('/the-news-of-the-day.html')




    # seccion-2
    def render_section_2(self):
        return render_template('sections/section-2.html')
    # subseccion-2
    def render_entrevista_map(self):
        return render_template('index.html')

    def render_agua_simulador(self):
        return render_template('/water-level-simulator.html',flag_1="opcion_2",flag_2="opcion_2")




    # seccion-3
    def render_section_3(self):
        return render_template('sections/section-3.html')
    # subseccion-3
    def render_diarios(self):
        return render_template('/diarios.html',flag_1="opcion_1",flag_2=" ")

    def render_shocking_photos(self):
        return render_template('/shocking-photos.html',flag_1="opcion_2",flag_2="opcion_2", impactantes=list_shocking)

    def render_during_flood(self):
        return render_template('/testimonio2.html',flag_1="opcion_4",flag_2="opcion_3")

    def render_photo_album(self):
        return render_template('/photo-album.html',flag_1="opcion_2",flag_2="opcion_2",flag_3="opcion_3", albums=list_album)





    # seccion-4
    def render_section_4(self):
        return render_template('sections/section-4.html')
    # subseccion-4
    def render_after_flood(self):
        return render_template('/testimonio3.html',flag_1="opcion_4",flag_2="opcion_3")

    def render_sandbox(self):
        return render_template('/sandbox.html')

    def render_why_do_we_flood(self):
        return render_template('/Why-do-we-flood.html')




    # seccion-5
    def render_section_5(self):
        return render_template('sections/section-5.html')
    # subseccion-5
    def render_recomendacion(self):
        return render_template('/recomendacion-como-actuar.html',flag_1="opcion_4",flag_2="opcion_3")

    def render_smart_survival(self):
        return render_template('/mochila-inteligente.html')

    def render_where_to_go(self):
        return render_template('/dondeir.html')

    def render_educational_games(self):
        return render_template('/juegos.html')




    # seccion-6
    def render_section_6(self):
        return render_template('sections/section-6.html')
    # subseccion-6
    def render_citadine_blue(self):
        return render_template('')

    def render_citadine_green(self):
        return render_template('')



    def render_inundacion_exterior(self):
        return render_template('/Inundaciones-en-el-exterior.html',flag_1="opcion_1",flag_2=" ")

    #subseccion-inundacion-exterior 
    def render_alemania(self):  
        return render_template('/inundacion-exterior/alemania.html')

    def render_chile(self):  
        return render_template('/inundacion-exterior/chile.html')   

    def render_polonia(self):  
        return render_template('/inundacion-exterior/polonia.html')  



    def render_conclusiones(self):
        return render_template('/Conclusiones-del-evento.html',flag_1="opcion_1",flag_2=" ")

    def render_conclusiones_radio(self):  
        return render_template('/conclusion-del-evento/la-ayuda-de-la-radio.html')   

    
    def render_conclusiones_solidaridad(self):  
        return render_template('/conclusion-del-evento/la-importancia-de-la-solidaridad.html')   


    def render_conclusiones_legado_memoria(self):  
        return render_template('/conclusion-del-evento/legado-memoria.html')   


    def render_conclusiones_reflexiones(self):  
        return render_template('/conclusion-del-evento/reflexiones-de-los-entrevistados.html')                                    
