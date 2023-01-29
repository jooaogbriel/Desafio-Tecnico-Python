# Desafio-Tecnico-Python
Interface web que aceita upload de arquivo CNAB, normaliza os dados e armazena-os em um banco de dados relacional, exibindo as informações em tela. 

## Linguagem e Tecnologias utilizadas no Projeto
* Python
* Framework Django
* SQlite3
* Views com Django Rest Framework
* ORM do Django
* Serializers
* Templates Django
* HTML
* CSS

## Ambiente


**2. Crie e ative o ambiente virtual**

digite os seguintes comandos no terminal:

```
python -m venv venv
source venv/bin/activate
```

**3. Instale os pacotes necessários para a aplicação funcionar perfeitamente**

`pip install -r requirements.txt`

**4. Rode as migrações**

`python manage.py migrate`


## Aplicação

**Execute o comando abaixo para iniciar o servidor**

`python manage.py runserver`

Existem duas URL's disponíveis para acesso:

1. **http://127.0.0.1:8000/data/upload/** - para fazer upload do arquivo CNAB
2. **http://127.0.0.1:8000/data/show/** - para ver as informações no banco de todos os arquivos CNAB que já foram enviados.
