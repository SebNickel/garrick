#!/usr/bin/env python
import sys
from colorama import init
from pick_db_file import pick_db_file
import db_connection
import card_repository
from review_cards import review_cards
from new_card import new_card
from new_cards import new_cards
import review
from user_colors import print_info, print_instruction, print_error
from usage_info import print_usage_info

def main():

    # Initialise colorama
    init()

    valid_args = ['-n', '-n2', '-s', '-s2', '-e', '-e2', '-b', '-bf', '-bb', '-bs', '-bl', '-br']

    if len(sys.argv) > 1 and sys.argv[1] not in valid_args:
        print_usage_info(sys.argv)        
        if sys.argv[1] not in ['-h', '--help']:
            sys.exit(1)
        sys.exit()

    db_file = pick_db_file()
    conn, cursor = db_connection.connect(db_file)
    card_repository.create_table_if_not_exists(conn, cursor)
    
    if len(sys.argv) == 1:
        table_is_empty = card_repository.check_if_empty(cursor)
        if table_is_empty:
            print_error("You don't have any cards yet.")
            print_instruction(
                'Create some cards by launching garrick with one of the following options first:'
            )
            print_instruction('\t-n\tCreate cards starting in one-way mode.')
            print_instruction('\t-n2\tCreate cards starting in two-way mode.')
            print_instruction('\t-s\tCreate cards starting in single-line and one-way mode.')
            print_instruction('\t-s2\tCreate cards starting in single-line and two-way mode.')
            print_instruction('\t-e\tCreate cards starting in editor mode and in one-way mode.')
            print_instruction('\t-s2\tCreate cards starting in editor mode and in two-way mode.')
        else:
            review.review(conn, cursor)
    elif sys.argv[1] == '-n':
        new_cards(conn, cursor, two_way_card=False, single_line_mode=False, editor_mode=False)
    elif sys.argv[1] == '-n2':
        new_cards(conn, cursor, two_way_card=True, single_line_mode=False, editor_mode=False)
    elif sys.argv[1] == '-s':
        new_cards(conn, cursor, two_way_card=False, single_line_mode=True, editor_mode=False)
    elif sys.argv[1] == '-s2':
        new_cards(conn, cursor, two_way_card=True, single_line_mode=True, editor_mode=False)
    elif sys.argv[1] == '-e':
        new_cards(conn, cursor, two_way_card=False, single_line_mode=False, editor_mode=True)
    elif sys.argv[1] == '-e2':
        new_cards(conn, cursor, two_way_card=True, single_line_mode=False, editor_mode=True)
    elif sys.argv[1] == '-b':
        review.browse_by_regex(conn, cursor) 
    elif sys.argv[1] == '-bf':
        review.browse_by_regex_front(conn, cursor) 
    elif sys.argv[1] == '-bb':
        review.browse_by_regex_back(conn, cursor) 
    elif sys.argv[1] == '-bs':
        review.browse_by_score(conn, cursor)
    elif sys.argv[1] == '-bl':
        review.browse_by_last_viewed(conn, cursor)
    elif sys.argv[1] == '-br':
        review.browse_by_last_viewed_reverse(conn, cursor)
    
    print_info('Kbai')
    
    db_connection.disconnect(conn, cursor)

if __name__ == '__main__':
    main()
