
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent #Define las rutas del proyecto 

class Config:
    #Configuración base de la aplicación.

    SECRET_KEY = os.environ.get("SK")
    POSTS_DIR = BASE_DIR / "_posts"


class TestingConfig(Config):
    #Configuración específica para las pruebas.

    TESTING = True
    SECRET_KEY = "Test-SK"
