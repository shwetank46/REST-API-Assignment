from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config
from flasgger import Swagger

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    # Swagger Config (IMPORTANT FIX)
    swagger_config = {
        "headers": [],
        "specs": [
            {
                "endpoint": 'apispec',
                "route": '/apispec.json',
                "rule_filter": lambda rule: True,
                "model_filter": lambda tag: True,
            }
        ],
        "static_url_path": "/flasgger_static",
        "swagger_ui": True,
        "specs_route": "/apidocs/"
    }

    Swagger(app, config=swagger_config)

    from src.routes.api import api_bp
    app.register_blueprint(api_bp)

    with app.app_context():
        db.create_all()

    return app