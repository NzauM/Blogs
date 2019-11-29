import os
class Config:
    '''
    Configuration parent class
    '''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:Moringa@localhost/blogs'

    # QUOTE_API_BASE_URL = 'http://quotes.stormconsultancy.co.uk/random.json'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.environ.get('SECRET_KEY')


class ProdConfig(Config):
    '''
    Configuration child class for production
    '''
    pass

class DevConfig(Config):
    '''
    Configuration child class for development
    '''
    
    DEBUG = True

Config_options = {
    'development' :DevConfig,
    'production' :ProdConfig
}
