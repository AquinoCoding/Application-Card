# Application-Docker-Flask-uWSGI

Docker container with uWSGI for Flask apps in Python 3

## Description

Ações da API

- Criar card
- Ler card
- Remover card
- Atualizar card
- Listar card
  - Filtrar por id o card
  - Filtrar por tags
  

- Criar tag
- Ler tag
- Remover tag
- Atualizar tag
- Listar tag
  - Filtrar por id a tag


## QuickStart

Para iniciar o build execute o seguinte comando dentro da pasta application

```
docker build -t application .
```

Para iniciar o container execute o seguinte comando dentro da pasta application


```
docker run -p 5000:5000 application
```

Ficará disponivel na Rota seguinte

```
curl -v "http://localhost:5000/"
``` 
