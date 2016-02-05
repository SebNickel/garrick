import card_repository
from card import Card
from get_timestamp import get_timestamp

prompt = '] '

def read_input():

    lines = []

    while True:
        try:
            line = input(prompt)
            lines.append(line)
        except KeyboardInterrupt:
            return None
        except EOFError:
            print(end = '\r')
            return '\n'.join(lines)

def menu(conn, cursor, two_way_card):

    print()
    print('q: Discard this card and quit.')
    print('d: Discard this card and start over.')
    print('t: Toggle two-way card and start over.')

    while True:
        selection = input('[q/d/t]: ')
        if selection in ['q', 'd', 't']:
            break
    
    if selection == 'q':
        return None
    
    if selection == 'd':
        return new_card(conn, cursor, two_way_card)

    if selection == 't':
        return new_card(conn, cursor, not two_way_card)

def new_card(conn, cursor, two_way_card):

    print('[Ctrl+D: Finish current side. Ctrl+C: Discard this card and get a menu.]')

    if two_way_card:
        print('Side 1:')
    else:
        print('Front:')
        
    front = read_input()
    if front == None:
        return menu(conn, cursor, two_way_card)

    if two_way_card:
        print('Side 2:')
    else:
        print('Back:')

    back = read_input()
    if back == None:
        return menu(conn, cursor, two_way_card)

    last_viewed = get_timestamp()

    new_card = Card(front, back, 0, last_viewed)
    card_repository.insert(conn, cursor, new_card)

    if two_way_card:
        flipped_card = Card(back, front, 0, last_viewed)
        card_repository.insert(conn, cursor, flipped_card)

    print('Saved.')

    return two_way_card
