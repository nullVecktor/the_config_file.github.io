
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

class Config:
    #Configuración base de la aplicación.

    SECRET_KEY = os.environ.get("SK")


class TestingConfig(Config):
    #Configuración específica para las pruebas.

    TESTING = True
    SECRET_KEY = "Test-SK"
