# models
from models.card_model import Cards
from models.tag_model import Tags

# services
from services.check_verify_bd import check_exist_tag


# db
from database.db_session import create_session

def insert_card(texto: str, tag: str):
    
    cards: Cards = Cards(texto=texto, tag=tag)
    
    with create_session() as session:
        session.add(cards)
        session.commit()

def insert_tag(name: str):
    
    if name == '': name = 'all'
    
    if check_exist_tag(name):
        return False
    
    tags: Tags = Tags(name=name)
    
    with create_session() as session:
        session.add(tags)
        session.commit()
            