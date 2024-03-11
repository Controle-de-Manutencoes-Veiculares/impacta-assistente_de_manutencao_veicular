from flask import Flask
from flask import render_template, redirect, jsonify , request
from app.models.Carcare import Veiculo
from app import db
from app.controllers.home_controller import HomeController

class CarroController:

    def form_carro(self):
        return render_template('posts/home/form_carro.html')

    def add_carro(self): 
        try:
            data = request.json  # Recebe os dados enviados no corpo da solicitação como JSON
            id_usuario = data.get("id_usuario")
            cor = data.get("cor")
            placa = data.get("placa")
            marca = data.get("marca")
            km = data.get("km")
            ano = data.get("ano")
            modelo = data.get("modelo")
            
            # Criação de uma instância do modelo Veiculo
            carro = Veiculo(id_cliente=id_usuario, cor=cor, placa=placa, marca=marca, km=km, ano=ano, modelo=modelo)
            
            # Adiciona o veículo à sessão do banco de dados
            db.session.add(carro)

            # Commit das alterações para salvar o veículo no banco de dados
            db.session.commit()

            # Redirecionamento para a rota index (ou qualquer outra rota que você deseje)
            return jsonify({'status': 'success', 'message': 'Veículo adicionado com sucesso'}), 200

        except Exception as e:
            # Se ocorrer um erro, reverta as alterações
            db.session.rollback()
            return jsonify({'status': 'error', 'message': str(e)}), 500

