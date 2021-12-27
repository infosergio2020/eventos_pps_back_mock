from flask import Blueprint

evento= Blueprint('evento',__name__)


#Defino la ruta para crear un evento
@evento.route('/evento')
def add_evento():
    return 'add evento'

