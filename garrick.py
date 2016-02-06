#!/usr/bin/env python
import sys
from pick_db_file import pick_db_file
import db_connection
import card_repository
from review_cards import review_cards
from new_card import new_card
from new_cards import new_cards

def main():

    db_file = pick_db_file()
    conn, cursor = db_connection.connect(db_file)
    card_repository.create_table_if_not_exists(conn, cursor)
    
    if len(sys.argv) == 1:
        table_is_empty = card_repository.check_if_empty(cursor)
        if table_is_empty:
            print("You don't have any cards yet.")
            print('Create some cards by launching garrick with one of the following options first:')
            print('\t-n\tcreate cards starting in one-way mode.')
            print('\t-n2\tcreate cards starting in two-way mode.')
            print('\t-s\tcreate cards starting in single-line and one-way mode.')
            print('\t-s2\tcreate cards stating in single-line and two-way mode.')
        else:
            review_cards(conn, cursor)
    elif sys.argv[1] == '-n':
        new_cards(conn, cursor, False, False)
    elif sys.argv[1] == '-n2':
        new_cards(conn, cursor, True, False)
    elif sys.argv[1] == '-s':
        new_cards(conn, cursor, False, True)
    elif sys.argv[1] == '-s2':
        new_cards(conn, cursor, True, True)
    else:
        print('Usage info coming soon.')
    
    print('Kbai')
    
    db_connection.disconnect(conn, cursor)

if __name__ == '__main__':
    main()
