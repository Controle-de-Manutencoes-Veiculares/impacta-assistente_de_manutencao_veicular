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
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')
    
    FlaskMVC(app)
    db.init_app(app)
    Migrate(app, db)

    from app.models.Carcare import Cliente, Veiculo, ClienteVeiculo, Pecas, VeiculoPecas
    return app

