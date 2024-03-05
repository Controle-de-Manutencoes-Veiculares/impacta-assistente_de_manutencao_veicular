from app import db

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)  # Defina um comprimento, por exemplo, 255 caracteres
    description = db.Column(db.Text, nullable=False)

    