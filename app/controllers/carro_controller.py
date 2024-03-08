from flask import render_template, redirect,request
from app.models.Carcare import Veiculo


class CarroController: 
    def form_carro(self):
        return render_template('posts/home/form_carro.html')

    def add_carro(self):
        # coletar dados do form via post
        apelido = request.form.get("apelido-carro")
        cor = request.form.get("cor-carro")
        placa = request.form.get("placa-carro")
        marca = request.form.get("marca-carro")
        km = request.form.get("km-carro")
        ano = request.form.get("ano-carro")
        modelo = request.form.get("modelo-carro")
        print(apelido)
        # regras para formulario incompleto

        # adicionar dados para tabela de veiculo (insert)
        db.execute("INSERT INTO car_care.veiculo ( cor, placa, marca, km, ano, modelo) VALUES ( ?, ?, ?, ?, ?,?)", cor, placa, marca, km, ano, modelo)
        # verificar redirecionamento para rota index
        return none

