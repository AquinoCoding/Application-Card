# models
from models.tag_model import Tags

# db
from database.db_session import create_session

def check_exist_tag(tag: str):
    
    # check existing tag
    with create_session() as session:
        
        tags: Tags = session.query(Tags).filter(Tags.name == tag).one_or_none()
                
        return tags
