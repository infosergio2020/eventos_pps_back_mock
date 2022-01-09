from config.db import db

lenguajes_programador = db.Table ('lenguajes_programador',
    db.Column('lenguaje_id',db.Integer, db.ForeignKey('lenguaje.id'), primary_key= True),
    db.Column('programador_id',db.Integer, db.ForeignKey('programador.id'), primary_key= True))