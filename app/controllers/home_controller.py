from flask import render_template
from app.models.Carcare import Veiculo
class HomeController:
    
    def index(self):
        veiculos = Veiculo.query.all()
        return render_template('pages/index.html', veiculos=veiculos)