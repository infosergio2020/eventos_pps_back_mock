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
    aux = dbms.get_eventos()

    return jsonify({'result': aux})
