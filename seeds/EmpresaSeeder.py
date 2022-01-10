# SEMILLA Y BASE DE DATOS
from flask_seeder import Seeder, Faker, generator
from config.db import db
# MODELO
from models.Empresa import Empresa


class DemoEmpresa(Seeder):

    def __init__(self, db=None):
        super().__init__(db=db)
        self.priority = 1

    def run(self):
        # Create a new Faker and tell it how to create User objects
        faker = Faker( cls=Empresa,
                        init={
                                "id": generator.Sequence(),
                                "nombre": generator.Name(),
                                "fundacion": generator.Name()
                            })
        
        for empresa in faker.create(5):
          print("Adding Empresa: %s" % empresa)
          self.db.session.add(empresa)