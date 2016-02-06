from card import Card
from get_timestamp import get_timestamp
from edit import edit
from colored_output import print_info, print_side, print_instruction, colored_prompt, colored_getpass

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

def compose_in_editor(two_way_card):

    if two_way_card:
        print_info('Two-way mode is ON.')
    else:
        print_info('Two-way mode is OFF.')
    print_instruction('Hit Enter to continue in editor mode, or enter one of these options:')
    print_instruction('q: Quit.')
    print_instruction('t: Toggle two-way card and continue in editor mode.')
    print_instruction('m: Continue in normal multi-line mode.')
    print_instruction('s: Continue in single-line mode.')
    while True:
        selection = colored_prompt('[q/t/m/s]: ')
        if selection in ['q', 't', 'm', 's', '']:
            break

    if selection == 'q':
        return None, None, None, None

    if selection == 't':
        two_way_card = not two_way_card

    if selection == 'm':
        return new_card(two_way_card, False, False)

    if selection == 's':
        return new_card(two_way_card, True, False)

    else:

        bogus_timestamp = '1991-08-25 20:57:08'
        empty_card = Card('', '', 0, bogus_timestamp)

        card = edit(empty_card, two_way_card)

        return card, two_way_card, False, True

def menu(two_way_card, single_line_mode, editor_mode):

    print()
    print_instruction('q: Discard this card and quit.')
    print_instruction('d: Discard this card and start over.')
    print_instruction('t: Toggle two-way card and start over.')
    print_instruction('s: Toggle single-line mode and start over.')
    print_instruction('e: Toggle editor-mode and start over.')

    while True:
        selection = colored_prompt('[q/d/t/s/e]: ')
        if selection in ['q', 'd', 't', 's', 'e']:
            break
    
    if selection == 'q':
        return None, None, None, None
    
    if selection == 'd':
        return new_card(two_way_card, single_line_mode, editor_mode)

    if selection == 't':
        return new_card(not two_way_card, single_line_mode, editor_mode)

    if selection == 's':
        return new_card(two_way_card, not single_line_mode, editor_mode)

    if selection == 'e':
        return new_card(two_way_card, single_line_mode, not editor_mode)

def new_card(two_way_card, single_line_mode, editor_mode):

    if editor_mode:

        return compose_in_editor(two_way_card)

    else:

        if single_line_mode:
            print_instruction('[Ctrl+C: Discard this card and get a menu.]')
        else:
            print_instruction(
                '[Ctrl+D: Finish current side. Ctrl+C: Discard this card and get a menu.]'
            )

        if two_way_card:
            print_side('Side 1:')
        else:
            print_side('Front:')
            
        front = read_input(single_line_mode)
        if front == None:
            return menu(two_way_card, single_line_mode, editor_mode)

        if two_way_card:
            print_side('Side 2:')
        else:
            print_side('Back:')

        back = read_input(single_line_mode)
        if back == None:
            return menu(two_way_card, single_line_mode, editor_mode)

        last_viewed = get_timestamp()

        card = Card(front, back, 0, last_viewed)

        return card, two_way_card, single_line_mode, editor_mode
