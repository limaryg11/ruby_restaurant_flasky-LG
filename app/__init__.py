from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    
    app = Flask(__name__)

    from .models.restaurant import Restaurant

    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql+psycopg2://postgres:postgres@localhost:5432/restaurants_development"

    db.init_app(app)
    migrate.init_app(app, db)

    from .routes.restaurant import restaurant_bp
    app.register_blueprint(restaurant_bp)

    return app