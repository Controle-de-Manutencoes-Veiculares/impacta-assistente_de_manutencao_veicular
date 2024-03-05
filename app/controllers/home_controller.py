from flask import render_template
from app.models.post import Post
class HomeController:
    def index(self):
        posts = Post.query.all()
        return render_template('posts/index.html', posts=posts)
    
    def show(self, name):
        
        return f"olá {name} você está na home page"