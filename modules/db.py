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


   