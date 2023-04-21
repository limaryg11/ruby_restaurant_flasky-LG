from flask import Flask

def create_app():
    
    app = Flask(__name__)

    from .routes.restaurant import restaurant_bp
    app.register_blueprint(restaurant_bp)

    return app