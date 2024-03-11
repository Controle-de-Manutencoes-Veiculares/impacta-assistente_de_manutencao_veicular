from flask import render_template

from app.models.Carcare import Veiculo


class HomeController:
    def index(self):
       
        # puxar dados de veiculos
        veiculos = Veiculo.query.all()
        
        # puxar dados de alertas
        return render_template('posts/home/index.html', veiculos=veiculos)
    
    # def show(self, name):
        
    #     return f"olá {name} você está na home page"
