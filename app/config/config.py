import os
from dotenv import load_dotenv
from pathlib import Path


basedir = os.path.abspath(Path(__file__).parents[2])
load_dotenv(os.path.join(basedir, '.env'))

class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
    DEBUG = True
    CATALOGO_URL = os.environ.get('CATALOGO_DEV_URL')
    COMPRAS_URL = os.environ.get('COMPRAS_DEV_URL')
    PAGOS_URL = os.environ.get('PAGOS_DEV_URL')
    INVENTARIO_URL = os.environ.get('INVENTARIO_DEV_URL')
    CACHE_REDIS_HOST = os.environ.get('REDIS_HOST')
    CACHE_REDIS_PORT = os.environ.get('REDIS_PORT')
    CACHE_REDIS_DB = os.environ.get('REDIS_DB')
    CACHE_REDIS_PASSWORD = os.environ.get('REDIS_PASSWORD')

class TestingConfig(Config):
    TESTING = True

class ProductionConfig(Config):
    DEBUG = False
    TESTING = False
    CATALOGO_URL = os.environ.get('CATALOGO_PROD_URL')
    COMPRAS_URL = os.environ.get('COMPRAS_PROD_URL')
    PAGOS_URL = os.environ.get('PAGOS_PROD_URL')
    INVENTARIO_URL = os.environ.get('INVENTARIO_PROD_URL')
    CACHE_REDIS_HOST = os.environ.get('REDIS_HOST')
    CACHE_REDIS_PORT = os.environ.get('REDIS_PORT')
    CACHE_REDIS_DB = os.environ.get('REDIS_DB')
    CACHE_REDIS_PASSWORD = os.environ.get('REDIS_PASSWORD')

config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}