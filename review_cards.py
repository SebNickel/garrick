import db_connection
from pick_card import pick_card
from review_card import review_card
import card_repository
from colored_output import print_instruction, print_info

def review_cards(conn, cursor):

    while True:
        
        print_instruction('[Ctrl+C to quit.]')

        try:
            card = pick_card(conn, cursor)
            updated_card = review_card(card)

            if updated_card == None:
                card_repository.delete(conn, cursor, card)
                print_error('DELETED.')
                table_is_empty = card_repository.check_if_empty(cursor)
                if table_is_empty:
                    print_info('You have no more cards!')
                    break
            else:
                card_repository.insert(conn, cursor, updated_card)   
                card_repository.delete(conn, cursor, card)   

        except KeyboardInterrupt:
            print()
            break
