from flask import Flask, render_template, redirect,jsonify
from flask import request
from flask.helpers import flash, url_for
from flask_mysqldb import MySQL

app= Flask(__name__)
#mysql connection
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']=''
app.config['MYSQL_DB']='evento'
mysql=MySQL(app)

#necesito una clave secreta para mi sesion
app.secret_key='mysecretkey'

#colocar las rutas antes de correr el servidor
# LISTA TODAS LAS AREAS
@app.route('/listArea')
def list_area():
    cur=mysql.connection.cursor()
    cur.execute('SELECT * FROM areas')
    areas=cur.fetchall();
    mysql.connection.commit()
    return jsonify({"areas":areas})

# AGREGA AREAS NUEVAS
@app.route('/addArea', methods=['POST'] )
def add_area():
    if request.method=='POST':  
        nombre=request.json['nomb'] 
        descripcion=request.json['desc'] 
        lat_area=request.json['lat'] 
        lng_area=request.json['lng']

        cur=mysql.connection.cursor()
        cur.execute('INSERT INTO areas (nombre,descripcion,longitud,latitud) VALUES (%s,%s,%s,%s)',
        (nombre,descripcion,lng_area,lat_area))
        mysql.connection.commit()
        return jsonify({"message":"se agregó correctamente"})

@app.route('/editArea/<id>',methods=['POST'] )
def edit_area(id):
    if request.method=='POST':  
        nom_area=request.json['nomb'] 
        des_area=request.json['desc']
        lat_area=request.json['lat'] 
        lng_area=request.json['lng']

        
        cur=mysql.connection.cursor()
        cur.execute(""" 
        UPDATE areas
        SET nombre=%s,descripcion=%s,longitud=%s,latitud=%s
        WHERE id = %s
        """, (nom_area,des_area,lng_area,lat_area,id))
        mysql.connection.commit()
    return jsonify({"message":"se actulizo????"})


@app.route('/deleteArea/<id>')
def delete_area(id):
    cur=mysql.connection.cursor()
    cur.execute('DELETE FROM areas where id = {0}'.format(id))
    mysql.connection.commit()
    return jsonify({"message":"e ha eliminado el area","id":id})

# ---------------------------------------------------------------------
# ---------------------------------FOTOS--------------------------------
# ----------------------------------------------------------------------


# LISTA TODAS LAS AREAS
@app.route('/listFotos')
def list_fotos():
    cur=mysql.connection.cursor()
    cur.execute('SELECT * FROM foto')
    fotos=cur.fetchall();
    mysql.connection.commit()
    return jsonify({"fotos":fotos})

# AGREGA AREAS NUEVAS
@app.route('/addFoto', methods=['POST'] )
def add_foto():
    if request.method=='POST':  
        url_foto=request.json['url'] 
        descripcion=request.json['desc'] 

        cur=mysql.connection.cursor()
        cur.execute('INSERT INTO foto (url,descripcion) VALUES (%s,%s)',
        (url_foto,descripcion))
        mysql.connection.commit()
        return jsonify({"message":"se agregó correctamente"})

@app.route('/editFoto/<id>',methods=['POST'] )
def edit_foto(id):
    if request.method=='POST':  
        url=request.json['url'] 
        des=request.json['desc']

        
        cur=mysql.connection.cursor()
        cur.execute(""" 
        UPDATE foto
        SET url=%s,descripcion=%s
        WHERE id_foto = %s
        """, (url,des,id))
        mysql.connection.commit()
    return jsonify({"message":"se actualizo????"})


@app.route('/deleteFoto/<id>')
def delete_foto(id):
    cur=mysql.connection.cursor()
    cur.execute('DELETE FROM foto where id_foto = {0}'.format(id))
    mysql.connection.commit()
    return jsonify({"message":"e ha eliminado el foto","id":id})



# ---------------------------------------------------------------------
# ---------------------------------VIDEOS--------------------------------
# ----------------------------------------------------------------------




# LISTA TODAS LAS AREAS
@app.route('/listVideos')
def list_videos():
    cur=mysql.connection.cursor()
    cur.execute('SELECT * FROM video')
    videos=cur.fetchall();
    mysql.connection.commit()
    return jsonify({"videos":videos})

# AGREGA AREAS NUEVAS
@app.route('/addVideo', methods=['POST'] )
def add_video():
    if request.method=='POST':  
        url_video=request.json['url'] 
        descripcion=request.json['desc'] 

        cur=mysql.connection.cursor()
        cur.execute('INSERT INTO video (url,descripcion) VALUES (%s,%s)',
        (url_video,descripcion))
        mysql.connection.commit()
        return jsonify({"message":"se agregó correctamente"})

@app.route('/editVideo/<id>',methods=['POST'] )
def edit_video(id):
    if request.method=='POST':  
        url=request.json['url'] 
        des=request.json['desc']

        
        cur=mysql.connection.cursor()
        cur.execute(""" 
        UPDATE video
        SET url=%s,descripcion=%s
        WHERE id_video = %s
        """, (url,des,id))
        mysql.connection.commit()
    return jsonify({"message":"se actualizo????"})


@app.route('/deleteVideo/<id>')
def delete_video(id):
    cur=mysql.connection.cursor()
    cur.execute('DELETE FROM video where id_video = {0}'.format(id))
    mysql.connection.commit()
    return jsonify({"message":"se ha eliminado el foto","id":id})




if __name__=='__main__':
    app.run(port=4000,debug=True)
