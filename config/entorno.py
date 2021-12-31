from os import environ

class DevelopmentConfig:
    """Development configuration."""
    # FLASK
    ENV = "development"
    DEBUG = environ.get("DEBUG", True) #modo debug para flask
    # SQLALCHEMY / MYSQL    
    DB_HOST = environ.get("DB_HOST", "127.0.0.1") #nombre de la ip
    DB_USER = environ.get("DB_USER","root") #nombre de usuario
    DB_PASS = environ.get("DB_PASS","admin123") #contraseña para la conexion
    DB_NAME = environ.get("DB_NAME","eventos") #nombre del schema
    DB_TYPE = environ.get("DB_TYPE", "mysql") #nombre del motor de BD
    DB_PORT = environ.get("DB_PORT", "3306") #nro de puerto del servidor MSQL
    SQLALCHEMY_DATABASE_URI = f"{DB_TYPE}://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    SQLALCHEMY_ECHO = False # 
    SQLALCHEMY_TRACK_MODIFICATIONS = False #

config = DevelopmentConfig