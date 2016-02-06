import card_repository
from card import Card
from review_card import review_card
from colored_output import print_info, print_error, print_instruction, colored_prompt, colored_getpass

def browse(conn, cursor, results):

    count = len(results)

    if count == 0:
        print_error('No results.')
    elif count == 1:
        print_info('[1 RESULT.]')
    else:
        print_info('[{} RESULTS.]'.format(count))

    try:
        for row in results:

            card = Card(*row)
            updated_card = review_card(card)

            if updated_card == None:
                card_repository.delete(conn, cursor, card)
                print_error('DELETED.')
            else:
                card_repository.insert(conn, cursor, updated_card)
                card_repository.delete(conn, cursor, card)
            
            count -= 1

            if count > 0:
                print_info('[{} MORE.]'.format(count))

    except KeyboardInterrupt:
        print()

def browse_by_regex(conn, cursor):
    regex = colored_prompt('Enter regular expression: ')
    results = card_repository.select_by_regex(cursor, regex)
    browse(conn, cursor, results)

def browse_by_regex_front(conn, cursor):
    regex = colored_prompt('Enter regular expression: ')
    results = card_repository.select_by_regex_front(cursor, regex)
    browse(conn, cursor, results)

def browse_by_regex_back(conn, cursor):
    regex = colored_prompt('Enter regular expression: ')
    results = card_repository.select_by_regex_back(cursor, regex)
    browse(conn, cursor, results)

def browse_by_score(conn, cursor):
    score = colored_prompt('Show cards with the following score: ')
    results = card_repository.select_by_score(cursor, score)
    browse(conn, cursor, results)

def browse_by_last_viewed(conn, cursor):
    results = card_repository.select_by_last_viewed(cursor)
    browse(conn, cursor, results)

def browse_by_last_viewed_reverse(conn, cursor):
    results = card_repository.select_by_last_viewed_reverse(cursor)
    browse(conn, cursor, results)
