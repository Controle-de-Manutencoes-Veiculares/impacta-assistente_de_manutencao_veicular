from flask import render_template, redirect, request
from app.models.Carcare import Veiculo
from app import db
from app.controllers.home_controller import HomeController


class CarroController:

    def form_carro(self):
        return render_template('posts/home/form_carro.html')

    def add_carro():
        
        # coletar dados do form via post
        print(request.form.get("id_usuario-carro"))

        id_usuario = request.form.get("id_usuario-carro")
        cor = request.form.get("cor-carro")
        placa = request.form.get("placa-carro")
        marca = request.form.get("marca-carro")
        km = request.form.get("km-carro")
        ano = request.form.get("ano-carro")
        modelo = request.form.get("modelo-carro")
        
        # instanciar veiculo
        carro = veiculo(id_usuario=id_usuario, cor=cor, placa=placa, marca=marca, km=km, ano=ano, modelo=modelo)
        print(carro)
        
        # regras para formulario incompleto

        # adicionar dados para tabela de veiculo (insert)
        db.session.add(carro)
        db.session.commit()
        db.session.close()
        # db.execute("INSERT INTO car_care.veiculo ( cor, placa, marca, km, ano, modelo) VALUES ( ?, ?, ?, ?, ?,?)", cor, placa, marca, km, ano, modelo)
        
        # verificar redirecionamento para rota index
        return redirect ('/')

