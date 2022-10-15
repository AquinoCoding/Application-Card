import logging

from flask import Flask
from database.db_session import create_tables

from services.insert_bd import insert_tag


logging.basicConfig(
    format="[%(asctime)s.%(msecs)03d] [%(name)s] [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    level=logging.NOTSET
)

app = Flask(__name__)
db = create_tables()

populate_db = insert_tag('all')


from routes import cards
from routes import tags
from routes import docs
from routes import export_file
from routes import import_file

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)