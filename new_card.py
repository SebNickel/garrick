from card import Card
from get_timestamp import get_timestamp
from colored_output import print_info, print_instruction, colored_prompt, colored_getpass

prompt = '] '

def read_input(single_line_mode):

    lines = []

    try:
        if single_line_mode:
            line = colored_prompt(prompt)
            return line
        else:
            while True:
                try:
                    line = colored_prompt(prompt)
                    lines.append(line)
                except EOFError:
                    print(end = '\r')
                    return '\n'.join(lines)
    except KeyboardInterrupt:
        return None

def menu(conn, cursor, two_way_card, single_line_mode):

    print()
    print_instruction('q: Discard this card and quit.')
    print_instruction('d: Discard this card and start over.')
    print_instruction('t: Toggle two-way card and start over.')
    print_instruction('s: Toggle single-line mode and start over.')

    while True:
        selection = colored_prompt('[q/d/t/s]: ')
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
        print_instruction('[Ctrl+C: Discard this card and get a menu.]')
    else:
        print_instruction('[Ctrl+D: Finish current side. Ctrl+C: Discard this card and get a menu.]')

    if two_way_card:
        print_info('Side 1:')
    else:
        print_info('Front:')
        
    front = read_input(single_line_mode)
    if front == None:
        return menu(conn, cursor, two_way_card, single_line_mode)

    if two_way_card:
        print_info('Side 2:')
    else:
        print_info('Back:')

    back = read_input(single_line_mode)
    if back == None:
        return menu(conn, cursor, two_way_card, single_line_mode)

    last_viewed = get_timestamp()

    new_card = Card(front, back, 0, last_viewed)

    return new_card, two_way_card, single_line_mode
