from app import db

class Cliente(db.Model):
    id_cliente = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100))
    sexo = db.Column(db.String(100))
    nome = db.Column(db.String(100))
    cpf = db.Column(db.String(11))
    nascimento = db.Column(db.Date)
    contato = db.Column(db.Numeric)

class Veiculo(db.Model):
    id_veiculo = db.Column(db.Integer, primary_key=True)
    cor = db.Column(db.String(100))
    placa = db.Column(db.String(100))
    marca = db.Column(db.String(100))
    km = db.Column(db.Numeric)
    ano = db.Column(db.Numeric)
    modelo = db.Column(db.String(100))

class ClienteVeiculo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_cliente = db.Column(db.Integer, db.ForeignKey('cliente.id_cliente'))
    id_veiculo = db.Column(db.Integer, db.ForeignKey('veiculo.id_veiculo'))

class Pecas(db.Model):
    id_peca = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))
    km = db.Column(db.Numeric)

class VeiculoPecas(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_peca = db.Column(db.Integer, db.ForeignKey('pecas.id_peca'))
    id_veiculo = db.Column(db.Integer, db.ForeignKey('veiculo.id_veiculo'))
    