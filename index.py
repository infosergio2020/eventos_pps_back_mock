from app import app
from utils.db import db 

# app = MyApp().get_app()

with app.app_context():
    db.create_all() ## crear todas las tablas 

# # inicia app
if __name__=='__main__':
    app.run(debug=True)