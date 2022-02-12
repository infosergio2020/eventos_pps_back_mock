from flask import render_template,request

class CustomRouter:

    # index
    def render_index(self):
        return render_template('index.html');

    # secciones del sidebar
    def render_sections(self):
        return render_template('sidebar/sections.html');

    def render_announcements(self):
        return render_template('sidebar/announcements.html');

    def render_covid(self):
        return render_template('sidebar/covid.html');

    def render_about(self):
        return render_template('sidebar/about.html');

    def render_languaje(self):
        return render_template('sidebar/languaje.html');


    # secciones

    # seccion-1
    def render_section_1(self):
        return render_template('sections/section-1.html');

    # subseccion-1
    def render_before_flood(self):
        return render_template('');

    def render_noticias_dia(self):
        return render_template('');




    # seccion-2
    def render_section_2(self):
        return render_template('sections/section-2.html');
    # subseccion-2
    def render_entrevista_map(self):
        return render_template('');

    def render_agua_simulador(self):
        return render_template('');




    # seccion-3
    def render_section_3(self):
        return render_template('sections/section-3.html');
    # subseccion-3
    def render_diarios(self):
        return render_template('');

    def render_shocking_photos(self):
        return render_template('');

    def render_during_flood(self):
        return render_template('');

    def render_photo_album(self):
        return render_template('');





    # seccion-4
    def render_section_4(self):
        return render_template('sections/section-4.html');
    # subseccion-4
    def render_after_flood(self):
        return render_template('');

    def render_sandbox(self):
        return render_template('');

    def render_why_do_we_flood(self):
        return render_template('');




    # seccion-5
    def render_section_5():
        return render_template('sections/section-5.html');
    # subseccion-5
    def render_recomendacion():
        return render_template('');

    def render_smart_survival():
        return render_template('');

    def render_where_to_go():
        return render_template('');

    def render_educational_games():
        return render_template('');




    # seccion-6
    def render_section_6():
        return render_template('sections/section-6.html');
    # subseccion-6
    def render_citadine_blue():
        return render_template('');

    def render_citadine_green():
        return render_template('');

    def render_inundacion_exterior():
        return render_template('');

    def render_conclusiones():
        return render_template('');