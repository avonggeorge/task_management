"""
Initializes this parent directory as a python package
"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path

# Initialize database
db = SQLAlchemy()
DB_NAME = "database.db"

# Initialize flask
def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'Keepitsimple'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    # Tells flask the location of Blueprint
    from .routes import routes
    from .auth import auth

    # Register Blueprint
    app.register_blueprint(routes, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import User, Todos

    create_database(app)

    return app

# Create database if it does not exist
def create_database(app):
    if not path.exists('task_management/' + DB_NAME):
        with app.app_context():
            db.create_all()
            print('Created Database')
