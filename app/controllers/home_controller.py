from flask import render_template

class HomeController:
    def index(self):
        return render_template('posts/index.html')
    
    def show(self, name):
        
        return f"olá {name} você está na home page"