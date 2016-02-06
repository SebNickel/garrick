import card_repository
from card import Card
from review_card import review_card

def review_by_regex(conn, cursor, func):

    regex = input('Enter regular expression: ')

    results = func(regex)

    count = len(results)

    if count == 0:
        print('No results.')
    elif count == 1:
        print('1 result.')
    else:
        print('{} results.'.format(count))

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

def search_front(conn, cursor):
    func = lambda regex: card_repository.search_front(cursor, regex)
    review_by_regex(conn, cursor, func)

def search_back(conn, cursor):
    func = lambda regex: card_repository.search_back(cursor, regex)
    review_by_regex(conn, cursor, func)

def search_both_sides(conn, cursor):
    func = lambda regex: card_repository.search_both_sides(cursor, regex)
    review_by_regex(conn, cursor, func)
