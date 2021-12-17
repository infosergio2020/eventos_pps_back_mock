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
@app.route('/')
def Index():
    #establezco la coneccion
    cur=mysql.connection.cursor()
    #escribo la consulta
    cur.execute('SELECT * FROM foto')
   
    #ejecuto la busqueda de todas las fotos
    listado_foto=cur.fetchall();
    #escribo la consulta
    cur.execute('SELECT * FROM areas')
    #ejecuto la busqueda de todas las fotos
    listado_areas=cur.fetchall();
    
    return render_template('index.html',foto=listado_foto,areas=listado_areas)


@app.route('/add_foto', methods=['POST'] )
def add_foto():
    if request.method=='POST':  
        nom_foto=request.form['nombre_foto'] 
        des_foto=request.form['desc_foto'] 
        return jsonify({"nombre_foto":nom_foto , "desc_foto":des_foto})
        # #establezco la coneccion
        # cur=mysql.connection.cursor()
        # #escribo la consulta
        # cur.execute('INSERT INTO foto (url,descripcion) VALUES (%s,%s)',
        # (nom_foto,des_foto))
        # #ejecuto la consulta
        # mysql.connection.commit()
        # #aviso que se guardo correctamente en la base de datos
        # flash('Se ha guardado corectamente la foto')
        # # nota: return 'received' nos sirve para verificar que se inserto en la base de datos
        # return redirect(url_for('Index'))


@app.route('/edit/<id>' )
def get_area(id):
    #establezco la coneccion
    cur=mysql.connection.cursor()
    #escribo la consulta
    cur.execute('SELECT * FROM foto')
    #ejecuto la busqueda de todas las fotos
    listado_foto=cur.fetchall();
    #escribo la consulta
    cur.execute('SELECT * FROM areas where id = {0}'.format(id))
    #ejecuto la consulta
    area=cur.fetchall()[0]
    print(area)
    
    return render_template('editar.html',edit=area,fotos=listado_foto)

@app.route('/update/<string:id>',methods=['POST'] )
def update(id):
    if request.method=='POST':  
        nom_area=request.form['nombre_area'] 
        des_area=request.form['desc_area'] 
        id_f=request.form['opciones'][0]
        print(id_f)
         
        #establezco la coneccion
        cur=mysql.connection.cursor()
        #hago una consulta
        cur.execute(""" 
        UPDATE areas
        SET nombre=%s,descripcion=%s, id_foto=%s
        WHERE id = %s
        """, (nom_area,des_area,id_f,id))
    
        #ejecuto la consulta
        mysql.connection.commit()
        flash('Se ha actualizado el area '+ id)
        return redirect(url_for('Index'))

@app.route('/delete/<string:id>' )
def eliminar_area(id):
    #establezco la coneccion
    cur=mysql.connection.cursor()
    #escribo la consulta
    cur.execute('DELETE FROM areas where id = {0}'.format(id))
    #ejecuto la consulta
    mysql.connection.commit()
    flash('Se ha eliminado el area '+ id)
    return redirect(url_for('Index'))


@app.route('/add_foto', methods=['POST'] )
def add_foto():
    if request.method=='POST':  
        id_area_fk=request.form['are'][0]
        id_foto=request.form['opciones'][0]
        print(id_foto)

        #establezco la coneccion
        cur=mysql.connection.cursor()
        #hago una consulta
        cur.execute(""" 
        UPDATE foto
        SET id_area_fk=%s
        WHERE id = %s
        """, (id_area_fk,id_foto))
    
        #ejecuto la consulta
        mysql.connection.commit()
       
    
        #establezco la coneccion
        cur=mysql.connection.cursor()

        #escribo la consulta
        cur.execute('INSERT INTO foto (id_area_fk,id_foto) VALUES (%s,%s)',
        (id_area_fk,id_foto))
        #ejecuto la consulta
        mysql.connection.commit()
        #aviso que se guardo correctamente en la base de datos
        flash('Se ha guardado corectamente la foto')
        # nota: return 'received' nos sirve para verificar que se inserto en la base de datos
        return redirect(url_for('Index'))

if __name__=='__main__':
    app.run(port=4000,debug=True)
