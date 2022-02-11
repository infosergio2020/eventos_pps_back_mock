from os import environ

class DevelopmentConfig:
    """Development configuration."""
    # FLASK
    ENV = "development"
    DEBUG = environ.get("DEBUG", True) #modo debug para flask
    
config = DevelopmentConfig