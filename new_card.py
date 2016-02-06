from card import Card
from get_timestamp import get_timestamp

prompt = '] '

def read_input(single_line_mode):

    lines = []

    try:
        if single_line_mode:
            line = input(prompt)
            return line
        else:
            while True:
                try:
                    line = input(prompt)
                    lines.append(line)
                except EOFError:
                    print(end = '\r')
                    return '\n'.join(lines)
    except KeyboardInterrupt:
        return None

def menu(conn, cursor, two_way_card, single_line_mode):

    print()
    print('q: Discard this card and quit.')
    print('d: Discard this card and start over.')
    print('t: Toggle two-way card and start over.')
    print('s: Toggle single-line mode and start over.')

    while True:
        selection = input('[q/d/t/s]: ')
        if selection in ['q', 'd', 't', 's']:
            break
    
    if selection == 'q':
        return None, None, None
    
    if selection == 'd':
        return new_card(conn, cursor, two_way_card, single_line_mode)

    if selection == 't':
        return new_card(conn, cursor, not two_way_card, single_line_mode)

    if selection == 's':
        return new_card(conn, cursor, two_way_card, not single_line_mode)

def new_card(conn, cursor, two_way_card, single_line_mode):

    if single_line_mode:
        print('[Ctrl+C: Discard this card and get a menu.]')
    else:
        print('[Ctrl+D: Finish current side. Ctrl+C: Discard this card and get a menu.]')

    if two_way_card:
        print('Side 1:')
    else:
        print('Front:')
        
    front = read_input(single_line_mode)
    if front == None:
        return menu(conn, cursor, two_way_card, single_line_mode)

    if two_way_card:
        print('Side 2:')
    else:
        print('Back:')

    back = read_input(single_line_mode)
    if back == None:
        return menu(conn, cursor, two_way_card, single_line_mode)

    last_viewed = get_timestamp()

    new_card = Card(front, back, 0, last_viewed)

    return new_card, two_way_card, single_line_mode
