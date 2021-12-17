from flask import Flask,jsonify
from modules import db

app = Flask(__name__)
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']='admin123'
app.config['MYSQL_DB']='gestion_eventos'

dbms = db.DBConnection(app)

@app.route('/')
def index():
    
    # dbms.add_user('menem','bhjkhjgjghj','21423sedf@gmail')    
    # dbms.add_user('alfredo','123435436546','infoasdasd@gmail')
    # dbms.add_user('ricardio','345sdf','Tsdf2345@gmail')

    dbms.del_user_by_id(23)

    auxS = dbms.get_users()
    return jsonify({'result': auxS})
