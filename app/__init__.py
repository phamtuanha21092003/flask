from flask import Flask
from db import db
from config import Config
from flask_migrate import Migrate
from schemas import ma


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    db.init_app(app)
    ma.init_app(app)
    migrate = Migrate(app, db)

    # Initialize Flask extensions here

    # Register blueprints here
    from app.item import bp as item_bp
    app.register_blueprint(item_bp, url_prefix='/item')

    from app.store import bp as store_bp
    app.register_blueprint( store_bp, url_prefix='/store')

    return app