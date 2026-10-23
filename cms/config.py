
import os


class Config:
    #Configuración base de la aplicación.

    SECRET_KEY = os.environ.get()


class TestingConfig(Config):
    #Configuración específica para las pruebas.

    TESTING = True
    SECRET_KEY = ""
