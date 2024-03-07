from flask import render_template, redirect

class CarroController: 
    def form_carro(self):
        return render_template('posts/home/form_carro.html')

    def add_carro(self):
        # adicionar dados para tabela de veiculo
        # verificar redirecionamento para rota index
        return redirect('/index')

