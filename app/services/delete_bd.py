# libs
from datetime import datetime

# models
from models.card_model import Cards
from models.tag_model import Tags

# db
from database.db_session import create_session


def delete_card(id_: str):
    
    with create_session() as session:
        cards: Cards = session.query(Cards).filter(Cards.id == id_).one_or_none()
        
        if cards:
            session.delete(cards)
            session.commit()
            return True
        
        return False

def delete_tag(id_: str):
    
    with create_session() as session:
        tags: Tags = session.query(Tags).filter(Tags.id == id_).one_or_none()
        
        if tags:
            session.delete(tags)
            session.commit()
            return True

        return False
