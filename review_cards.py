import db_connection
from pick_card import pick_card
from review_card import review_card
import card_repository

def review_cards(conn, cursor):

    print('[Ctrl+C to quit.]')
    
    while True:
        try:
            row = pick_card(conn, cursor)
            updated_card = review_card(row)
            card_repository.update(conn, cursor, updated_card)   
        except KeyboardInterrupt:
            print()
            break
