from app import app

from services.read_bd import read_card

import csv

@app.route("/export")
def export_file():
    
    title = ['texto', 'tag']
    
    lista_cards = read_card()

    with open('./file-export.csv', 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=title, extrasaction='ignore') 
        writer.writeheader() 
        writer.writerows(lista_cards)
    
    return "<p>Export file completed</p>"
