
from flask import Flask

from cms.config import Config


def create_app(config_object=None):
    app = Flask(__name__)

    app.config.from_object(config_object or Config)

    from .routes import main
    app.register_blueprint(main)

    return app
