# TCC

Aplicativo para listar unidades próximas.


## Instalação de requisitos (NECESSÁRIO:Python 3.6.0+ e pip(Atualizado))

- Crie um ambiente virtual de sua preferência (Recomendado/Opcional)

- Faça um clone do projeto: `git clone https://github.com/alineBsoares/phonegap.git`

- Acesse o repositório: `cd phonegap/`

- Faça a instalação do `requirements.txt` usando o comando: `pip install -r requirements.txt`

## Rodando o server da API

- Acesse o projeto django com: `cd api`

- Rode as migrações do projeto: `python manage.py migrate`

- Crie um super user com: `python manage.py createsuperuser`

- Rode o servidor local com: `python manage.py runserver`

## Navegando pela API

- Faça login com o seu usuário em: `localhost:8000/admin`

- Acesse a root da API em: `localhost:8000/api/`

- Acesse lista de usuários em: `localhost:8000/api/user/`
