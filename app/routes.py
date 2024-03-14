from mvc_flask import Router

Router.get('/', 'home#index')
Router.get('/form-carro', 'veiculo#form_carro')

# Rotas CRUD carros
Router.get('/veiculo', 'veiculo#index')
Router.get('/veiculo/<id>', 'veiculo#show')
Router.post('/veiculo', 'veiculo#create')
Router.delete('/veiculo/<id>', 'veiculo#destroy')
Router.put('/veiculo/<id>', 'veiculo#update')

<<<<<<< HEAD
Router.get('/form-carro', 'carro#form_carro')

Router.post('/add-carro', 'carro#add_carro')

Router.post('/delete-carro', 'carro#delete_carro')
=======
>>>>>>> 285b85c57297e0a2f01fac112c96db4274890252
