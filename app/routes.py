from mvc_flask import Router

Router.get('/', 'home#index')

# Rotas CRUD carros
Router.get('/veiculo', 'veiculo#index')
Router.get('/veiculo/<id>', 'veiculo#show')
Router.post('/veiculo', 'veiculo#create')
Router.delete('/veiculo/<id>', 'veiculo#destroy')
Router.put('/veiculo/<id>', 'veiculo#update')

