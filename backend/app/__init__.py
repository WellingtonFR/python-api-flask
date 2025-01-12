from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from dotenv import load_dotenv
import os
from flask_migrate import Migrate


db = SQLAlchemy()

def create_app():

    # Initialize Flask app
    app = Flask(__name__)

    #Apply CORS
    CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}})

    # Initialize Flask-Migrate
    migrate = Migrate(app, db)

    # Load environment variables
    load_dotenv()

    # Configurations
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize extensions
    db.init_app(app)

    # Register routes
    from .routes import app as routes_blueprint
    app.register_blueprint(routes_blueprint)

    # Register models
    with app.app_context():
        from . import models
        db.create_all()

    return app
