import os

class Config:
    '''
    General configuration parent class
    '''
    
    
    #  email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    pass
class ProdConfig(Config):
    '''
    Production configuration 

    Args:
    Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    # if SQLALCHEMY_DATABASE_URI.startswith("postgres://"):
    #     SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI.replace("postgres://", "postgresql://")
   


class DevConfig(Config):
    '''\c 
    Development configuration child class

    Args: 
    Config The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:josie@localhost/moviez'
    DEBUG = True

class TestConfig(Config):
   SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:josie@localhost/moviez'



config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig
}
  
