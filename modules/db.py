from flask_mysqldb import MySQL
"""singleton class to deal with db"""

class DBConnection:
    def __init__(self,app_aux):
        self.mysql = MySQL(app_aux)
        self.query_select = ''' select * from {0}'''
        self.query_delete = ''' delete from {0} where {2} = {1}'''

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
        cur.execute(self.query_delete.format('user',iduser,"user.iduser"))
        self.mysql.connection.commit()
        

    def up_user(self,iduser,name,pwd,email):
        query = '''
            UPDATE user
            SET name = %s , pass = %s , email = %s
            WHERE iduser = %s
        '''
        cur = self.mysql.connection.cursor()
        cur.execute(query,(name,pwd,email,iduser))
        self.mysql.connection.commit()
        

    #///////////////
#     Nota: Juego con el area, nosotros debemos contemplar el caso de que el usuario no agregue un mismo juego otra vez. DESDE EL BACKEND
# Recordar: El recorrido de la base de datos en base a las insersiones es el siguiente:
# 1) Primero se debe agregar un evento.
# 2) Luego se pueden crear redSocial, Area, Foto, enVivo y Video
# 3) Si se tiene Area creado anteriormente se puede crear Juego.
# 4) Por ultimo, se pueden crear las tablas que tienen relacion con area 
# (video,foto) y evento (video,foto):
#  area_has_foto, area_has_video, evento_has_foto y evento_has_video . (editado)
# [19:23]
    #///////////////
    #///CRUD EVENTO///
    #///////////////

    def get_eventos(self):
        """get_eventos(self) -> eventos"""
        cur = self.mysql.connection.cursor()
        query = '''
                    SELECT nomEvento,lugarEvento,descEvento,DATE_FORMAT(fechaEvento, "%d/%m/%Y"),TIME_FORMAT(horaEvento, "%H:%i %p") FROM evento
                    
                '''
        cur.execute(query)
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
    #Primero eliminar las relaciondes del evento y a lo ultimo se puede eliminar el evento#
    def del_evento_by_id(self,idEvento):
        """ del_evento_by_id(self,idEvento) -> elimina un evento """
        cur = self.mysql.connection.cursor()
        cur.execute(self.query_delete.format('evento_has_foto',idEvento,'evento_has_foto.evento_idEvento'))
        cur.execute(self.query_delete.format('evento_has_video',idEvento,'evento_has_video.evento_idEvento'))
        cur.execute(self.query_delete.format('evento',idEvento,'evento.idEvento'))
        self.mysql.connection.commit()


    def up_evento(self,nombre,lugar,descripcion,fecha,hora,idEvento):
        query = '''
            UPDATE evento
            SET nomEvento = %s,lugarEvento = %s,descEvento = %s, fechaEvento = %s, horaEvento = %s
            WHERE idEvento = %s
        '''
        cur = self.mysql.connection.cursor()
        cur.execute(query,(nombre,lugar,descripcion,fecha,hora,idEvento))
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
        cur.execute(self.query_delete.format('redsocial',idRedsocial,'redsocial.idRedsocial'))
        self.mysql.connection.commit()

    
    def up_redsocial(self,nombreRed,idRedsocial):
        query = '''
            UPDATE redsocial
            SET nombreRed = %s
            WHERE idRedsocial = %s
        '''
        cur = self.mysql.connection.cursor()
        cur.execute(query,(nombreRed,idRedsocial))
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
        """ del_evento_by_id(self,idEvento) -> elimina un evento """
        cur = self.mysql.connection.cursor()
        cur.execute(self.query_delete.format('area_has_foto',idArea,'area_has_foto.area_idArea'))
        cur.execute(self.query_delete.format('area_has_video',idArea,'area_has_video.area_idArea'))
        cur.execute(self.query_delete.format('area',idArea,'area.idArea'))
        self.mysql.connection.commit()

    def up_area(self,nombre,descripcion,lng,lat,idRedsocial):
        query = '''
            UPDATE area
            SET nomArea = %s,descArea = %s,lngArea = %s,latArea = %s
            WHERE idArea = %s
        '''
        cur = self.mysql.connection.cursor()
        cur.execute(query,(nombre,descripcion,lng,lat,idRedsocial))
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

        cur.execute(self.query_delete.format('evento_has_foto',idFoto,'evento_has_foto.foto_idFoto'))
        cur.execute(self.query_delete.format('area_has_foto',idFoto,'area_has_foto.foto_idFoto'))

        cur.execute(self.query_delete.format('foto',idFoto,"foto.idFoto"))
        self.mysql.connection.commit()


    def up_foto(self,titulo,url,descripcion,idFoto):
        query = '''
            UPDATE foto
            SET tituloF = %s,urlF = %s,descF = %s
            WHERE idFoto = %s 
        '''
        cur = self.mysql.connection.cursor()
        cur.execute(query,(titulo,url,descripcion,idFoto))
        self.mysql.connection.commit()

   #///////////////
    #///CRUD ENVIVO///
    #///////////////

    def get_envivos(self):
        """get_envivos(self) -> envivos"""
        cur = self.mysql.connection.cursor()
        query = '''
                    SELECT nomEnvivo ,urlEnvivo,descEnvivo,DATE_FORMAT(fechaEnvivo, "%d/%m/%Y"),TIME_FORMAT(horaEnvivo, "%H:%i %p") FROM envivo
                '''
        cur.execute(query)
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
        cur.execute(self.query_delete.format('envivo',idEnvivo,"envivo.idEnvivo"))
        self.mysql.connection.commit()

    def up_envivo(self,nombre,url,descripcion,fecha,hora,idEnvivo):
        query = '''
            UPDATE envivo
            SET nomEnvivo = %s,urlEnvivo = %s,descEnvivo = %s,fechaEnvivo = %s,horaEnvivo = %s
            WHERE idEnvivo = %s
        '''
        cur = self.mysql.connection.cursor()
        cur.execute(query,(nombre,url,descripcion,fecha,hora,idEnvivo))
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
        cur.execute(self.query_delete.format('evento_has_video',idVideo,'evento_has_video.video_idVideo'))
        cur.execute(self.query_delete.format('area_has_video',idVideo,'area_has_video.video_idVideo'))

        cur.execute(self.query_delete.format('video',idVideo,"video.idVideo"))
        self.mysql.connection.commit()

    def up_video(self,tituloV,urlV,descV,idVideo):
        query = '''
            UPDATE video
            SET tituloV=%s, urlV = %s,descV = %s
            WHERE idVideo = %s
        '''
        cur = self.mysql.connection.cursor()
        cur.execute(query,(tituloV,urlV,descV,idVideo))
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
        cur.execute(self.query_delete.format('juego',idJuego,"juego.idJuego"))
        self.mysql.connection.commit()

    def up_juego(self,nomJuego,urlJuego,urlImgJuego,descJuego,idJuego):
        query = '''
            UPDATE juego
            SET nomJuego= %s, urlJuego= %s, urlImgJuego= %s,descJuego = %s
            WHERE idJuego = %s 
            '''
        cur = self.mysql.connection.cursor()
        cur.execute(query,(nomJuego,urlJuego,urlImgJuego,descJuego,idJuego))
        self.mysql.connection.commit()  

