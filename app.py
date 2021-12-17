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
    # dbms.del_user_by_id(23)

    # dbms.add_area("area-1","soy el area-1 descripcion randmon",2021.1001,2021.1001,2),
    # dbms.add_area("area-2","soy el area-2 descripcion randmon",202.11002,2021.1001,4),
    # dbms.add_area("area-3","soy el area-3 descripcion randmon",2021.1003,2021.1001,1),
    # dbms.add_area("area-4","soy el area-4 descripcion randmon",20.211004,2021.1001,3),
    # dbms.add_area("area-5","soy el area-5 descripcion randmon",23.211004,2231.1001,3)

    dbms.del_area_by_id(4)
    aux = dbms.get_areas()

    return jsonify({'result': aux})
