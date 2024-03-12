from flask import render_template, redirect, jsonify , request, flash
from app.models.Carcare import Veiculo
from app import db
from app.controllers.home_controller import HomeController

class VeiculoController:

    def form_carro(self):
        return render_template('posts/home/form_carro.html')

    def index(self):
        try:
            veiculos = Veiculo.query.all()
            veiculos_json = [veiculo.serialize() for veiculo in veiculos]
            return jsonify({'status': 'success', 'content': veiculos_json}), 200
        except Exception as e:
            return jsonify({'status': 'error', 'message': str(e)}), 500
    
    def show(self, id):
        try:
            # Encontra o veículo pelo ID
            carro = Veiculo.query.get(id)
            if carro:
                # Se o veículo foi encontrado, serializa o veículo e o retorna em JSON
                carro_json = carro.serialize()
                return jsonify({'status': 'success', 'content': carro_json}), 200
            else:
                # Se o veículo não foi encontrado, retorna uma mensagem de erro
                return jsonify({'status': 'error', 'message': 'Veículo não encontrado'}), 404
        except Exception as e:
            # Se ocorrer algum erro, retorna uma resposta JSON de erro
            return jsonify({'status': 'error', 'message': str(e)}), 500

    def create(self): 
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
            # return redirect('/')??
            return jsonify({'status': 'success', 'message': 'Veículo adicionado com sucesso'}), 201
            

        except Exception as e:
            # Se ocorrer um erro, reverta as alterações
            db.session.rollback()
            return jsonify({'status': 'error', 'message': str(e)}), 500
    
    def destroy(self, id):
        try:
            # Encontra o veículo pelo ID
            carro = Veiculo.query.get(id)

            if carro:
                # Remove o veículo da sessão do banco de dados
                db.session.delete(carro)
                
                # Commit das alterações para remover o veículo do banco de dados
                db.session.commit()

                return jsonify({'status': 'success', 'message': 'Veículo removido com sucesso'}), 200
            else:
                return jsonify({'status': 'error', 'message': 'Veículo não encontrado'}), 404

        except Exception as e:
            # Se ocorrer um erro, reverta as alterações
            db.session.rollback()
            return jsonify({'status': 'error', 'message': str(e)}), 500

    