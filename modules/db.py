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
        """ del_area_by_id(self,idarea) -> elimina un area """
        cur = self.mysql.connection.cursor()
        cur.execute(self.query_delete.format('area',idArea))
        self.mysql.connection.commit()


   