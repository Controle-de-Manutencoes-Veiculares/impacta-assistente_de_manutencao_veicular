from flask import Flask
from mvc_flask import FlaskMVC
#from flask_sqlalchemy import SQLAlchemy
#from flask_migrate import Migrate

#db =SQLAlchemy()

def create_app():
    app = Flask(__name__)
    FlaskMVC(app)
    
    # app.config['SQLALCHEMY_DATABASE_URI'] = "url_mySQL"
    # db.init_app(app)
    # Migrate(app, db)

    # from app.models.post import Post

    return app

