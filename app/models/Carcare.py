from app import db

class Cliente(db.Model):
    id_cliente = db.Column(db.Integer, primary_key=True, autoincrement=True, unique=True) #incluso autoincremento e unique
    email = db.Column(db.String(100))
    sexo = db.Column(db.String(100))
    nome = db.Column(db.String(100))
    cpf = db.Column(db.String(11), unique=True)
    nascimento = db.Column(db.Date)#formato - atual ano-mes-dia
    contato = db.Column(db.Numeric)#ajustar tamanho

class Veiculo(db.Model):
    id_veiculo = db.Column(db.Integer, primary_key=True, autoincrement=True, unique=True) #incluso autoincremento e unique
    id_cliente = db.Column(db.Integer, db.ForeignKey('cliente.id_cliente'))
    cor = db.Column(db.String(100))
    placa = db.Column(db.String(100))
    marca = db.Column(db.String(100))
    km = db.Column(db.Numeric)
    ano = db.Column(db.Numeric)
    modelo = db.Column(db.String(100))

    def __init__(self, id_cliente, cor, placa, marca, km, ano, modelo):
        self.id_cliente = id_cliente
        self.cor = cor
        self.placa = placa
        self.marca = marca
        self.km = km
        self.ano = ano
        self.modelo = modelo    

    def serialize(self):
        return {
            'id_veiculo': self.id_veiculo,
            'id_cliente': self.id_cliente,
            'cor': self.cor,
            'placa': self.placa,
            'marca': self.marca,
            'km': self.km,
            'ano': self.ano,
            'modelo': self.modelo
        }	

class Pecas(db.Model):
    id_peca = db.Column(db.Integer, primary_key=True, autoincrement=True) #incluso autoincremento
    nome = db.Column(db.String(100))
    km = db.Column(db.Numeric)

class VeiculoPecas(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True) #incluso autoincremento
    id_peca = db.Column(db.Integer, db.ForeignKey('pecas.id_peca'))
    id_veiculo = db.Column(db.Integer, db.ForeignKey('veiculo.id_veiculo'))
