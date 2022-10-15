from app import app
from flask import render_template, request, jsonify

# libs
import json
import time
from datetime import datetime

# services
from services.check_verify_bd import check_exist_tag

from services.insert_bd import insert_card
from services.read_bd import read_card, read_card_filter, read_card_single
from services.edit_bd import edit_card
from services.delete_bd import delete_card

# db
from database.db_session import create_session

# models
from models.card_model import Cards
from models.tag_model import Tags


# add Card
@app.route("/card", methods=["POST"])
def add_card():
    
    try:
        texto = request.json["texto"]
        tag = request.json["tag"]
        
    except Exception as e:
        return {"datetime": datetime.today(),
                "error": f"Todos os parametros são obrigatorios"}
        
    if tag == '': tag = 'all'
    
    for i_tag in tag.split(";"):
        tags = check_exist_tag(i_tag)
        if not tags: return {"datetime": datetime.today(),
                            "error": f'{i_tag} não encontrada'}

    insert_card(texto, tag)
        
    return {"datetime": datetime.today(),
            "mensagem": "Adição concluida com sucesso"}

# all Cards
@app.route("/card", methods=["GET"])
def get_cards():
         
    content_cards = read_card()

    return {"datetime": datetime.today(),
            "data": content_cards}

# filter tags all card
@app.route("/card/tag=<tag>", methods=["GET"])
def get_cards_filter_(tag):
    
    # check existing tag
    tags = check_exist_tag(tag)

    if not tags: return {"datetime": datetime.today(),
                        "error": 'tag não encontrada'}
            
    content_cards = read_card_filter(tag)

    return {"datetime": datetime.today(),
            "data": content_cards}

# single Card
@app.route("/card/<id_>", methods=["GET"])
def get_card(id_):
    
    cards = read_card_single(id_)
    
    if not cards: return {"datetime": datetime.today(),
                        "mensagem": "Não encontrado"}

    return {"datetime": datetime.today(),
            "data": {"id": cards.id, "texto": cards.texto, 
                    "tag": cards.tag, "creat_date": cards.creat_date, 
                    "data_modificacao": cards.data_modificacao}}

# Update Card
@app.route("/card/<id_>", methods=["PUT"])
def update_card(id_):
    
    try:
        texto = request.json["texto"]
        tag = request.json["tag"]
    
    except Exception as e: 
        return {"datetime": datetime.today(),
                "error": f"Confira os parametros obrigatorios"}

        
    tags = check_exist_tag(tag)
        
    if not tags: return {"datetime": datetime.today(),
                        "error": 'tag não encontrada'}
    
    edit_card(id_, texto, tag)

    return {"datetime": datetime.today(),
            "mensagem": "Alteracao concluida com sucesso"}

# Delete Card
@app.route("/card/<id_>", methods=["DELETE"])
def del_card(id_):
    
    if delete_card(id_):
        return {"datetime": datetime.today(),
                "mensagem": "Delete concluido com sucesso"}
    
    else: return {"datetime": datetime.today(),
                      "mensagem": "Não encontrado"}
