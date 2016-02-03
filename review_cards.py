import db_connection
from pick_card import pick_card
from review_card import review_card
import card_repository

def review_cards(conn, cursor):

    while True:
        
        print('[Ctrl+C to quit.]')

        try:
            card = pick_card(conn, cursor)
            updated_card = review_card(card)

            if updated_card == None:
                card_repository.delete(conn, cursor, card)
                print('Deleted.')
                table_is_empty = card_repository.check_if_empty(cursor)
                if table_is_empty:
                    print('You have no more cards!')
                    break
            else:
                card_repository.replace(conn, cursor, card, updated_card)   

        except KeyboardInterrupt:
            print()
            break
