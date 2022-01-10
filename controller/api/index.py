from flask import jsonify,request
from controller import test

def indexF():
    test.init_db()
    return jsonify(res="OK")