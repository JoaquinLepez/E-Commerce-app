from flask import Flask
import os
from app.config import config


def create_app():
    app_context = os.getenv("FLASK_CONTEXT")
    print(f"app_context: {app_context}")

    app = Flask(__name__)
    configuration = config[app_context if app_context else 'development']
    app.config.from_object(configuration)

    from app.resource import e_commerce
    app.register_blueprint(e_commerce, url_prefix='/api/v1')

    return app

