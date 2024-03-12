from mvc_flask import Router

Router.get('/', 'home#index')
Router.get('/form-carro', 'veiculo#form_carro')

# Rotas CRUD carros
Router.get('/veiculo', 'veiculo#index')
Router.get('/veiculo/<id>', 'veiculo#show')
Router.post('/veiculo', 'veiculo#create')
Router.delete('/veiculo/<id>', 'veiculo#destroy')
Router.put('/veiculo/<id>', 'veiculo#update')

