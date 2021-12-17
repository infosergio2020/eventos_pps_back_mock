from flask_mysqldb import MySQL
"""singleton class to deal with db"""

class DBConnection:
    def __init__(self,app_aux):
        self.mysql = MySQL(app_aux)
        self.query_select = ''' select * from {0}'''
        self.query_delete = ''' delete from {0} where {0}.iduser = {1}'''

# OPERACIONES DE LA BASE DE DATOS
    def get_users(self):
        cur = self.mysql.connection.cursor()
        cur.execute(self.query_select.format('user'))
        return cur.fetchall()

        
    def add_user(self,name,pswd,email):
        cur = self.mysql.connection.cursor()
        query = '''
                    INSERT INTO user (name,pass,email) 
                    VALUES (%s,%s,%s)
                '''
        data = (name,pswd,email)
        cur.execute(query,data)
        self.mysql.connection.commit()

    def del_user_by_id(self,iduser):
        cur = self.mysql.connection.cursor()
        cur.execute(self.query_delete.format('user',iduser))
        self.mysql.connection.commit()

