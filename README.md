# 🚗AutoCare - Controle de Manutenções Veiculares
Este é um projeto desenvolvido pelos alunos da Faculdade Impacta, como parte de um trabalho acadêmico para a matéria de Software Product: Analysis, Specification, Projec. O objetivo deste projeto é criar um sistema web para controle de manutenções veiculares, proporcionando uma maneira eficiente de gerenciar as atividades de manutenção de uma frota de veículos.

## 🛠️Funcionalidades
- **Cadastro de Veículos:** Permite adicionar informações detalhadas sobre os veículos da frota, como modelo, marca, ano, placa, entre outros.
- **Registro de Manutenções:** Possibilita o registro de todas as manutenções realizadas em cada veículo, incluindo data, tipo de serviço, peças substituídas, custo, e informações do fornecedor, se aplicável.
- **Agendamento de Manutenções:** Permite agendar manutenções futuras com base em quilometragem, tempo decorrido ou necessidades específicas do veículo.
- **Alertas e Notificações:** Envio de alertas e notificações automáticas para os responsáveis pela manutenção dos veículos, lembrando-os de manutenções agendadas, vencimento de garantias, entre outros.
- **Relatórios e Estatísticas:** Geração de relatórios e estatísticas sobre o histórico de manutenções, custos, tempo de atividade dos veículos, entre outros indicadores relevantes.

## 🛠️Tecnologias Utilizadas
**Frontend:** HTML5, CSS3, JavaScript (Framework a ser definido)<br/>
**Backend:** Python ( com uso das bibliotecas Flask, mvc_flask, Flask SQLAlchemy, Flask Migrate ), banco de dados MySQL<br/>
**Autenticação e Autorização:** JSON Web Tokens (JWT) para autenticação de usuários e controle de acesso às funcionalidades do sistema.<br/>
**Notificações:** Integração com serviços de envio de e-mails ou mensagens SMS para notificações automáticas.<br/>
**Controle de Versão:** Git para controle de versão do código fonte, hospedado em um repositório remoto (por exemplo, GitHub).

## 🤝Como Contribuir
Para contribuir com este projeto, siga os passos abaixo:

- Clone o repositório para o seu ambiente local (git clone [<url do repositório>](https://github.com/Controle-de-Manutencoes-Veiculares/impacta-assistente_de_manutencao_veicular.git)]).
- Crie uma branch para suas alterações (git checkout -b feature/nome-da-sua-feature).
- Faça suas alterações e adicione commits descrevendo-as de forma clara.
- Empurre suas alterações para o seu repositório no GitHub (git push origin feature/nome-da-sua-feature).
- Abra um pull request para a branch master.


# 🏗️Dependências do Projeto
Este projeto requer algumas dependências específicas para serem instaladas. Você pode instalá-las usando o gerenciador de pacotes pip. Certifique-se de que está em um ambiente virtual Python antes de instalar as dependências.
Dependências Principais
As seguintes são as dependências principais do projeto:

-**Flask:** Um framework web leve para Python.
```
pip install Flask==3.0.0
```

**mvc_flask:** Um pacote para implementar o padrão MVC (Model-View-Controller) em aplicações Flask.
```
pip install mvc_flask
```

**Flask SQLAlchemy:** Um ORM (Object-Relational Mapping) para Flask que facilita a interação com bancos de dados SQL.
```
pip install Flask-SQLAlchemy
```

**Flask Migrate:** Uma extensão para Flask SQLAlchemy que facilita a migração de bancos de dados.
```
pip install Flask-Migrate
```

## Como rodar localmente
- Apóes clonar o repositório, e instalar todas as dependências, inicializar o servidor flask pelo terminal
```
run flask
```
  
# 👥Equipe de Desenvolvimento
Caique Camargo Moreno <br/>
Gabrielli Quintino de Castro<br/>
Leonardo Souza<br/>
Marcos Vinicius Martins Lopes<br/>
Vanessa Aparecida Costa<br/>
Rafael Sen<br/>
Rodrigo Santos Moraes
