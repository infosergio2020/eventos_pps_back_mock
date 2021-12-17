from flask_mysqldb import MySQL
"""singleton class to deal with db"""

class DBConnection:
    def __init__(self,app_aux):
        self.mysql = MySQL(app_aux)
        self.query_select = ''' select * from {0}'''
        self.query_delete = ''' delete from {0} where {0}.iduser = {1}'''

# OPERACIONES DE LA BASE DE DATOS
    #///////////////
    #///CRUD USER///
    #///////////////

    def get_users(self):
        """get_users(self) -> areas"""
        cur = self.mysql.connection.cursor()
        cur.execute(self.query_select.format('user'))
        return cur.fetchall()

        
    def add_user(self,name,pswd,email):
        """add_user(self,name,pswd,email) -> añade un usuario"""
        cur = self.mysql.connection.cursor()
        query = '''
                    INSERT INTO user (name,pass,email) 
                    VALUES (%s,%s,%s)
                '''
        data = (name,pswd,email)
        cur.execute(query,data)
        self.mysql.connection.commit()

    def del_user_by_id(self,iduser):
        """ del_user_by_id(self,iduser) -> elimina un usuario """
        cur = self.mysql.connection.cursor()
        cur.execute(self.query_delete.format('user',iduser))
        self.mysql.connection.commit()

    #///////////////
#     Nota: Juego con el area, nosotros debemos contemplar el caso de que el usuario no agregue un mismo juego otra vez. DESDE EL BACKEND
# Recordar: El recorrido de la base de datos en base a las insersiones es el siguiente:
# 1) Primero se debe agregar un evento.
# 2) Luego se pueden crear redSocial, Area, Foto, enVivo y Video
# 3) Si se tiene Area creado anteriormente se puede crear Juego.
# 4) Por ultimo, se pueden crear las tablas que tienen relacion con area (video,foto) y evento (video,foto): area_has_foto, area_has_video, evento_has_foto y evento_has_video . (editado)
# [19:23]
    #///////////////
    #///CRUD EVENTO///
    #///////////////

    def get_eventos(self):
        """get_eventos(self) -> eventos"""
        cur = self.mysql.connection.cursor()
        cur.execute(self.query_select.format('evento'))
        return cur.fetchall()

        
    def add_evento(self,nomEvento,lugarEvento,descEvento,fechaEvento,horaEvento):
        """add_evento(self,nomEvento,lugarEvento,descEvento,fechaEvento,horaEvento) -> añade un evento"""
        cur = self.mysql.connection.cursor()
        query = '''
                    INSERT INTO evento (nomEvento,lugarEvento,descEvento,fechaEvento,horaEvento) 
                    VALUES (%s,%s,%s,%s,%s)
                '''
        data = (nomEvento,lugarEvento,descEvento,fechaEvento,horaEvento)
        cur.execute(query,data)
        self.mysql.connection.commit()

    def del_evento_by_id(self,idEvento):
        """ del_evento_by_id(self,idEvento) -> elimina un evento """
        cur = self.mysql.connection.cursor()
        cur.execute(self.query_delete.format('evento',idEvento))
        self.mysql.connection.commit()


    #///////////////
    #///CRUD REDSOCIAL///
    #///////////////

    def get_redsocial(self):
        """get_redsocial(self) -> redsocial"""
        cur = self.mysql.connection.cursor()
        cur.execute(self.query_select.format('redsocial'))
        return cur.fetchall()

        
    def add_redsocial(self,nombreRed,evento_idEvento):
        """add_redsocial(self,nombreRed,evento_idEvento) -> añade una redsocial"""
        cur = self.mysql.connection.cursor()
        query = '''
                    INSERT INTO redsocial (nombreRed,evento_idEvento) 
                    VALUES (%s,%s)
                '''
        data = (nombreRed,evento_idEvento)
        cur.execute(query,data)
        self.mysql.connection.commit()

    def del_redsocial_by_id(self,idRedsocial):
        """ del_redsocial_by_id(self,idRedsocial) -> elimina una redsocial """
        cur = self.mysql.connection.cursor()
        cur.execute(self.query_delete.format('redsocial',idRedsocial))
        self.mysql.connection.commit()

    #///////////////
    #///CRUD AREA///
    #///////////////

    def get_areas(self):
        """get_areas(self) -> areas"""
        cur = self.mysql.connection.cursor()
        cur.execute(self.query_select.format('area'))
        return cur.fetchall()

        
    def add_area(self,nomArea,descArea,lngArea,latArea, evento_idEvento):
        """add_area(self,nomArea,descArea,lngArea,latArea, evento_idEvento) -> añade un area"""
        cur = self.mysql.connection.cursor()
        query = '''
                    INSERT INTO area (nomArea,descArea,lngArea,latArea, evento_idEvento) 
                    VALUES (%s,%s,%s,%s,%s)
                '''
        data = (nomArea,descArea,lngArea,latArea, evento_idEvento)
        cur.execute(query,data)
        self.mysql.connection.commit()

    def del_area_by_id(self,idArea):
        """ del_area_by_id(self,idArea) -> elimina un area """
        cur = self.mysql.connection.cursor()
        cur.execute(self.query_delete.format('area',idArea))
        self.mysql.connection.commit()


   #///////////////
    #///CRUD FOTO///
    #///////////////

    def get_fotos(self):
        """get_fotos(self) -> fotos"""
        cur = self.mysql.connection.cursor()
        cur.execute(self.query_select.format('foto'))
        return cur.fetchall()

        
    def add_foto(self,tituloF,urlF,descF):
        """add_foto(self,tituloF,urlF,descF) -> añade una foto"""
        cur = self.mysql.connection.cursor()
        query = '''
                    INSERT INTO foto (tituloF,urlF,descF) 
                    VALUES (%s,%s,%s)
                '''
        data = (tituloF,urlF,descF)
        cur.execute(query,data)
        self.mysql.connection.commit()

    def del_foto_by_id(self,idFoto):
        """ del_foto_by_id(self,idFoto) -> elimina una foto """
        cur = self.mysql.connection.cursor()
        cur.execute(self.query_delete.format('foto',idFoto))
        self.mysql.connection.commit()


   #///////////////
    #///CRUD ENVIVO///
    #///////////////

    def get_envivos(self):
        """get_envivos(self) -> envivos"""
        cur = self.mysql.connection.cursor()
        cur.execute(self.query_select.format('envivo'))
        return cur.fetchall()

        
    def add_envivo(self,nomEnvivo,urlEnvivo,descEnvivo,fechaEnvivo,horaEnvivo, evento_idEvento):
        """add_envivo(self,nomEnvivo,urlEnvivo,descEnvivo,fechaEnvivo,horaEnvivo, evento_idEvento) -> añade un envivo"""
        cur = self.mysql.connection.cursor()
        query = '''
                    INSERT INTO envivo (nomEnvivo,urlEnvivo,descEnvivo,fechaEnvivo,horaEnvivo, evento_idEvento) 
                    VALUES (%s,%s,%s,%s,%s,%s)
                '''
        data = (nomEnvivo,urlEnvivo,descEnvivo,fechaEnvivo,horaEnvivo, evento_idEvento)
        cur.execute(query,data)
        self.mysql.connection.commit()

    def del_envivo_by_id(self,idEnvivo):
        """ del_envivo_by_id(self,idEnvivo) -> elimina un envivo """
        cur = self.mysql.connection.cursor()
        cur.execute(self.query_delete.format('envivo',idEnvivo))
        self.mysql.connection.commit()

   

   #///////////////
    #///CRUD VIDEO///
    #///////////////

    def get_videos(self):
        """get_videos(self) -> videos"""
        cur = self.mysql.connection.cursor()
        cur.execute(self.query_select.format('video'))
        return cur.fetchall()

        
    def add_video(self,tituloV,urlV,descV):
        """add_video(self,tituloV,urlV,descV) -> añade un video"""
        cur = self.mysql.connection.cursor()
        query = '''
                    INSERT INTO video (tituloV,urlV,descV) 
                    VALUES (%s,%s,%s)
                '''
        data = (tituloV,urlV,descV)
        cur.execute(query,data)
        self.mysql.connection.commit()

    def del_video_by_id(self,idVideo):
        """ del_video_by_id(self,idVideo) -> elimina un video """
        cur = self.mysql.connection.cursor()
        cur.execute(self.query_delete.format('video',idVideo))
        self.mysql.connection.commit()

   #///////////////
    #///CRUD JUEGO///
    #///////////////

    def get_juegos(self):
        """get_juegos(self) -> juegos"""
        cur = self.mysql.connection.cursor()
        cur.execute(self.query_select.format('juego'))
        return cur.fetchall()

        
    def add_juego(self,nomJuego,urlJuego,descJuego,urlImgJuego,area_idArea):
        """add_juego(self,nomJuego,urlJuego,descJuego,urlImgJuego,area_idArea) -> añade un juego"""
        cur = self.mysql.connection.cursor()
        query = '''
                    INSERT INTO juego (nomJuego,urlJuego,descJuego,urlImgJuego,area_idArea) 
                    VALUES (%s,%s,%s,%s,%s)
                '''
        data = (nomJuego,urlJuego,descJuego,urlImgJuego,area_idArea)
        cur.execute(query,data)
        self.mysql.connection.commit()

    def del_juego_by_id(self,idJuego):
        """ del_juego_by_id(self,idJuego) -> elimina un juego """
        cur = self.mysql.connection.cursor()
        cur.execute(self.query_delete.format('juego',idJuego))
        self.mysql.connection.commit()

   #FALTA COLOCAR ESTAS TABLAS: area_has_foto, area_has_video, evento_has_foto y evento_has_video

      #///////////////
    #///CRUD TABLA area_has_foto///
    #///////////////

    def get_area_has_fotos(self):
        """get_area_has_fotos(self) -> area_has_fotos"""
        cur = self.mysql.connection.cursor()
        cur.execute(self.query_select.format('area_has_foto'))
        return cur.fetchall()

        
    def add_area_has_foto(self,area_idArea,foto_idFoto):
        """add_area_has_foto(self,area_idArea,foto_idFoto) -> añade un area_has_foto"""
        cur = self.mysql.connection.cursor()
        query = '''
                    INSERT INTO area_has_foto (area_idArea,foto_idFoto) 
                    VALUES (%s,%s)
                '''
        data = (area_idArea,foto_idFoto)
        cur.execute(query,data)
        self.mysql.connection.commit()

#
#
#    El eliminar de la tabla area_has_foto no tiene un id propio como para eliminarlo
#   Discutir como eliminariamos esta tabla.
#
    def del_area_has_foto_by_id(self,idarea_has_foto):
        """ del_area_has_foto_by_id(self,idarea_has_foto) -> elimina un area_has_foto """
        cur = self.mysql.connection.cursor()
        cur.execute(self.query_delete.format('area_has_foto',idarea_has_foto))
        self.mysql.connection.commit()


  #///////////////
    #///CRUD TABLA area_has_video///
    #///////////////

    def get_area_has_videos(self):
        """get_area_has_videos(self) -> area_has_videos"""
        cur = self.mysql.connection.cursor()
        cur.execute(self.query_select.format('area_has_video'))
        return cur.fetchall()

        
    def add_area_has_video(self,area_idArea,video_idVideo):
        """add_area_has_video(self,area_idArea,video_idVideo) -> añade un area_has_video"""
        cur = self.mysql.connection.cursor()
        query = '''
                    INSERT INTO area_has_video (area_idArea,video_idVideo) 
                    VALUES (%s,%s)
                '''
        data = (area_idArea,video_idVideo)
        cur.execute(query,data)
        self.mysql.connection.commit()

#
#
#    El eliminar de la tabla area_has_video no tiene un id propio como para eliminarlo
#   Discutir como eliminariamos esta tabla.
#
    def del_area_has_video_by_id(self,idarea_has_video):
        """ del_area_has_video_by_id(self,idarea_has_video) -> elimina un area_has_video """
        cur = self.mysql.connection.cursor()
        cur.execute(self.query_delete.format('area_has_video',idarea_has_video))
        self.mysql.connection.commit()


#///////////////
    #///CRUD TABLA evento_has_foto///
    #///////////////

    def get_evento_has_fotos(self):
        """get_evento_has_fotos(self) -> evento_has_fotos"""
        cur = self.mysql.connection.cursor()
        cur.execute(self.query_select.format('evento_has_foto'))
        return cur.fetchall()

        
    def add_evento_has_foto(self,evento_idEvento,foto_idFoto):
        """add_evento_has_foto(self,evento_idEvento,foto_idFoto) -> añade un evento_has_foto"""
        cur = self.mysql.connection.cursor()
        query = '''
                    INSERT INTO evento_has_foto (evento_idEvento,foto_idFoto) 
                    VALUES (%s,%s)
                '''
        data = (evento_idEvento,foto_idFoto)
        cur.execute(query,data)
        self.mysql.connection.commit()

#
#
#    El eliminar de la tabla evento_has_foto no tiene un id propio como para eliminarlo
#   Discutir como eliminariamos esta tabla.
#
    def del_evento_has_foto_by_id(self,idevento_has_foto):
        """ del_evento_has_foto_by_id(self,idevento_has_foto) -> elimina un evento_has_foto """
        cur = self.mysql.connection.cursor()
        cur.execute(self.query_delete.format('evento_has_foto',idevento_has_foto))
        self.mysql.connection.commit()


#///////////////
    #///CRUD TABLA evento_has_video ///
    #///////////////

    def get_evento_has_videos(self):
        """get_evento_has_videos(self) -> evento_has_videos"""
        cur = self.mysql.connection.cursor()
        cur.execute(self.query_select.format('evento_has_video'))
        return cur.fetchall()

        
    def add_evento_has_video(self,evento_idEvento,video_idVideo):
        """add_evento_has_video(self,evento_idEvento,video_idVideo) -> añade un evento_has_video"""
        cur = self.mysql.connection.cursor()
        query = '''
                    INSERT INTO evento_has_video (evento_idEvento,video_idVideo) 
                    VALUES (%s,%s)
                '''
        data = (evento_idEvento,video_idVideo)
        cur.execute(query,data)
        self.mysql.connection.commit()

#
#
#    El eliminar de la tabla evento_has_video no tiene un id propio como para eliminarlo
#   Discutir como eliminariamos esta tabla.
#
    def del_evento_has_video_by_id(self,idevento_has_video):
        """ del_evento_has_video_by_id(self,idevento_has_video) -> elimina un evento_has_video """
        cur = self.mysql.connection.cursor()
        cur.execute(self.query_delete.format('evento_has_video',idevento_has_video))
        self.mysql.connection.commit()
