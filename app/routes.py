from mvc_flask import Router

Router.get('/', 'home#index')

Router.get('/form-carro', 'carro#form_carro')

Router.post('/add-carro', 'carro#add_carro')

Router.all('posts', only='show')