from app import app
from config.db import db 
# from flask_seeder import FlaskSeeder
# app = MyApp().get_app()

with app.app_context():
    db.create_all() ## crear todas las tablas 


# # inicia app
if __name__=='__main__':
    
    # seeder = FlaskSeeder()
    # seeder.init_app(app, db)
    app.run()
    