from flask import Flask, render_template, redirect,jsonify
from flask import request
from flask.helpers import flash, url_for

app= Flask(__name__)
#necesito una clave secreta para mi sesion
app.secret_key='mysecretkey'

#colocar las rutas antes de correr el servidor
@app.route('/')
def Index():
    
    return render_template('index.html')


if __name__=='__main__':
    app.run(port=4000,debug=True)
