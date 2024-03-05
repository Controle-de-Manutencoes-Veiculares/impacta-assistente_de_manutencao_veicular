from flask import Flask
from mvc_flask import FlaskMVC
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
import os

db =SQLAlchemy()

def create_app():
    
    load_dotenv()
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:123456@localhost:3306/car_care"
    
    FlaskMVC(app)
    db.init_app(app)
    Migrate(app, db)

    from app.models.post import Post
    return app

