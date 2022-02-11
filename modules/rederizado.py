from flask import render_template,request

class CustomRouter:

    # index
    def render_index():
        return render_template('index.html');

    # secciones del sidebar
    def render_sections():
        return render_template('sidebar/sections.html');

    def render_announcements():
        return render_template('sidebar/announcements.html');

    def render_covid():
        return render_template('sidebar/covid.html');

    def render_about():
        return render_template('sidebar/about.html');

    def render_languaje():
        return render_template('sidebar/languaje.html');


    # secciones

    # seccion-1
    def render_section_1():
        return render_template('sections/section-1.html');

    # subseccion-1
    def render_before_flood():
        return render_template('');

    def render_noticias_dia():
        return render_template('');




    # seccion-2
    def render_section_2():
        return render_template('sections/section-2.html');
    # subseccion-2
    def render_entrevista_map():
        return render_template('');

    def render_agua_simulador():
        return render_template('');




    # seccion-3
    def render_section_3():
        return render_template('sections/section-3.html');
    # subseccion-3
    def render_diarios():
        return render_template('');

    def render_shocking_photos():
        return render_template('');

    def render_during_flood():
        return render_template('');

    def render_photo_album():
        return render_template('');





    # seccion-4
    def render_section_4():
        return render_template('sections/section-4.html');
    # subseccion-4
    def render_after_flood():
        return render_template('');

    def render_sandbox():
        return render_template('');

    def render_why_do_we_flood():
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