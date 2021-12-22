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
    # aux = dbms.add_user("juancito","123gregve","juan@gmail.com")
    # aux = dbms.add_redsocial("nombreRedFACElol3",3)
    # aux = dbms.add_area("soyAreaSuper4","descAreaSUper4","12434","425434",4)
    # aux = dbms.add_envivo("soy un envivo super","https://www.youtube.com/watch?v=Hy7Qf5myfX0","descEnvivo super","12/11/12","12:04:12","1")
    # aux = dbms.add_juego("soy un juego super","https://www.youtube.com/watch?v=Hy7Qf5myfX0","descjuego super","https://www.youtube.com/watch?v=Hy7Qf5myfX0",1)
    aux = dbms.del_user_by_id(1)
    

    return jsonify({'result': aux})
# OPERACIONES DE LA BASE DE DATOS
    #///////////////
    #///CRUD USER///
    #///////////////

# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         return do_the_login()
#     else:
#         return show_the_login_form()