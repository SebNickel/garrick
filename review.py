import card_repository
from card import Card
from edit import edit
from iterators import review_iterator, browsing_iterator
from review_card import review_card
from user_colors import print_info, print_instruction, print_error, colored_prompt

def include_flipped_card(cursor, card):

    print_info('This is a two-way card.')
    print_info('Should your changes also affect the flipped version of this card?')
    while True:
        answer = colored_prompt('[y/n]: ')
        if answer in ['y', 'n']:
            break
    if answer == 'y':
        return True
    else:
        return False

def iterate(conn, cursor, iterator, count):

    if count == 0:
        print_error('No results.')
    elif count == 1:
        print_info('[1 CARD.]')
    else:
        print_info('[{} CARDS.]'.format(count))

    try:
        for card in iterator:

            print_instruction('[Ctrl+C to quit.]')

            updated_card, contents_changed = review_card(card)

            is_two_way_card = card_repository.is_two_way_card(cursor, card)

            if is_two_way_card and contents_changed:
                flipped_card_too = include_flipped_card(cursor, card)
            else:
                flipped_card_too = False

            if updated_card == None:
                card_repository.delete(conn, cursor, card)
                if flipped_card_too:
                    card_repository.delete_flipped_card(conn, cursor, card)
                    count -= 1
                # Not an error, but I feel this should be red.
                print_error('DELETED.')
                table_is_empty = card_repository.check_if_empty(cursor)
                if table_is_empty:
                    print_info('You have no more cards!')
                    break
            else:
                if contents_changed:

                    while True:
                        card_repository.insert(conn, cursor, updated_card)
                        if flipped_card_too:
                            card_repository.insert_flipped_card(conn, cursor, updated_card)
                        print_instruction('Create another version based on this same card?')
                        print_info('Protip: This is how you split one card into several cards.')
                        while True:
                            answer = colored_prompt('[y/n]: ')
                            if answer in ['y', 'n']:
                                break
                        if answer == 'n':
                            break
                        else:
                            updated_card = edit(card, flipped_card_too)

                    card_repository.delete(conn, cursor, card)
                    if flipped_card_too:
                        card_repository.delete_flipped_card(conn, cursor, card)
                else:
                    card_repository.insert(conn, cursor, updated_card)
                    card_repository.delete(conn, cursor, card)
            
            count -= 1

            if count > 0:
                print_info('[{} MORE:]'.format(count))

    except KeyboardInterrupt:
        print()

def review(conn, cursor):
    count = card_repository.count(cursor)
    iterator = review_iterator(conn, cursor)
    iterate(conn, cursor, iterator, count)

def browse(conn, cursor, results):
    count = len(results)
    iterator = browsing_iterator(results)
    iterate(conn, cursor, iterator, count)

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
