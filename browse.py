import card_repository
from card import Card
from review_card import review_card

def browse(conn, cursor, results):

    count = len(results)

    if count == 0:
        print('No results.')
    elif count == 1:
        print('[1 RESULT.]')
    else:
        print('[{} RESULTS.]'.format(count))

    try:
        for row in results:

            card = Card(*row)
            updated_card = review_card(card)

            if updated_card == None:
                card_repository.delete(conn, cursor, card)
                print('DELETED.')
            else:
                card_repository.insert(conn, cursor, updated_card)
                card_repository.delete(conn, cursor, card)
            
            count -= 1

            if count > 0:
                print('[{} MORE.]'.format(count))

    except KeyboardInterrupt:
        print()

def browse_by_regex(conn, cursor):
    regex = input('Enter regular expression: ')
    results = card_repository.select_by_regex(cursor, regex)
    browse(conn, cursor, results)

def browse_by_regex_front(conn, cursor):
    regex = input('Enter regular expression: ')
    results = card_repository.select_by_regex_front(cursor, regex)
    browse(conn, cursor, results)

def browse_by_regex_back(conn, cursor):
    regex = input('Enter regular expression: ')
    results = card_repository.select_by_regex_back(cursor, regex)
    browse(conn, cursor, results)

def browse_by_score(conn, cursor):
    score = input('Show cards with the following score: ')
    results = card_repository.select_by_score(cursor, score)
    browse(conn, cursor, results)

def browse_by_last_viewed(conn, cursor):
    results = card_repository.select_by_last_viewed(cursor)
    browse(conn, cursor, results)

def browse_by_last_viewed_reverse(conn, cursor):
    results = card_repository.select_by_last_viewed_reverse(cursor)
    browse(conn, cursor, results)
