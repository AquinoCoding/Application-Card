# Application Flask


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


## QuickStart Docker

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

## QuickStart Local

Para rodar o projeto é necessário criar o ambiente virtual com o seguinte comando

```
python3 -m venv env
```

Entre no ambiente virtual no meu caso eu acesso com source

```
env/bin/activate
```

Para outras OS pode ser de outra maneira como 

```
env/Scripts/Activate
```

Agora vamos instalar os requirements. No terminal acesse o diretorio em que o arquivo requirements.txt está e execute o seguinte comando 

```
pip install -r requirements.txt
```

Agora inicialize o app com o seguinte comando.

```
python3 app/wsgi.py
```

O projeto ficará disponível na porta 5000, certifique-se de que a porta não está sendo utilizada.
