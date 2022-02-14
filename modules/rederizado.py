from flask import render_template,request

class CustomRouter:

    # index
    def render_index(self):
        return render_template('index.html')

    # secciones del sidebar
    def render_sections(self):
        return render_template('sidebar/sections.html')

    def render_announcements(self):
        return render_template('sidebar/anounce.html')

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
        return render_template('/testimonio1.html')

    def render_noticias_dia(self):
        return render_template('/the-news-of-the-day.html')




    # seccion-2
    def render_section_2(self):
        return render_template('sections/section-2.html')
    # subseccion-2
    def render_entrevista_map(self):
        return render_template('index.html')

    def render_agua_simulador(self):
        return render_template('/water-level-simulator.html')




    # seccion-3
    def render_section_3(self):
        return render_template('sections/section-3.html')
    # subseccion-3
    def render_diarios(self):
        return render_template('/diarios.html')

    def render_shocking_photos(self):
        return render_template('/shocking-photos.html')

    def render_during_flood(self):
        return render_template('/testimonio2.html')

    def render_photo_album(self):
        return render_template('/photo-album.html')





    # seccion-4
    def render_section_4(self):
        return render_template('sections/section-4.html')
    # subseccion-4
    def render_after_flood(self):
        return render_template('/testimonio3.html')

    def render_sandbox(self):
        return render_template('/sandbox.html')

    def render_why_do_we_flood(self):
        return render_template('/Why-do-we-flood.html')




    # seccion-5
    def render_section_5(self):
        return render_template('sections/section-5.html')
    # subseccion-5
    def render_recomendacion(self):
        return render_template('/recomendacion-como-actuar.html')

    def render_smart_survival(self):
        return render_template('')

    def render_where_to_go(self):
        return render_template('')

    def render_educational_games(self):
        return render_template('')




    # seccion-6
    def render_section_6(self):
        return render_template('sections/section-6.html')
    # subseccion-6
    def render_citadine_blue(self):
        return render_template('')

    def render_citadine_green(self):
        return render_template('')



    def render_inundacion_exterior(self):
        return render_template('/Inundaciones-en-el-exterior.html')

    #subseccion-inundacion-exterior 
    def render_alemania(self):  
        return render_template('/inundacion-exterior/alemania.html')

    def render_chile(self):  
        return render_template('/inundacion-exterior/chile.html')   

    def render_polonia(self):  
        return render_template('/inundacion-exterior/polonia.html')  



    def render_conclusiones(self):
        return render_template('/Conclusiones-del-evento.html')

    def render_conclusiones_radio(self):  
        return render_template('/conclusion-del-evento/la-ayuda-de-la-radio.html')   

    
    def render_conclusiones_solidaridad(self):  
        return render_template('/conclusion-del-evento/la-importancia-de-la-solidaridad.html')   


    def render_conclusiones_legado_memoria(self):  
        return render_template('/conclusion-del-evento/legado-memoria.html')   


    def render_conclusiones_reflexiones(self):  
        return render_template('/conclusion-del-evento/reflexiones-de-los-entrevistados.html')                                    
