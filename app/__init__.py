from flask import Flask
from flask_caching import Cache
import os
from app.config import config, cache_config

cache = Cache()

def create_app():
    app_context = os.getenv("FLASK_CONTEXT")
    print(f"app_context: {app_context}")

    app = Flask(__name__)
    configuration = config[app_context if app_context else 'development']
    app.config.from_object(configuration)

    cache_configuration = cache_config[app_context if app_context else 'development']
    cache.init_app(app, config=cache_configuration)

    from app.resources import e_commerce
    app.register_blueprint(e_commerce, url_prefix='/api/v1')

    return app

