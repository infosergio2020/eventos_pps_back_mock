from utils.db import db

tabla_len_user=db.Table('tabla_len_user',
                        db.Column('area_id',db.Integer, db.ForeignKey('area.id'),primary_key=True),
                        db.Column('user_id',db.Integer, db.ForeignKey('user.iduser'),primary_key=True)
 )
