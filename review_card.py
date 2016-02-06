from card import Card
import card_repository
from unescape import unescape
from get_timestamp import get_timestamp
from edit import edit
from colored_output import print_instruction, colored_prompt, colored_getpass

def menu(card):
    
    print_instruction('e: Edit this card.')
    print_instruction('d: Delete this card.')

    while True:
        selection = colored_prompt('[e/d]: ')
        if selection in ['e', 'd']:
            break

    if selection == 'e':
        return edit(card)
    elif selection == 'd':
        return None

def review_card(card):
    
    front = unescape(card.front)
    back = unescape(card.back)

    print(front)
    colored_getpass('[Enter to flip the card.]')
    print(back)

    while True:
        score = colored_prompt("[Score yourself from 0 to 5, or enter 'o' for options:] ")
        if score == 'o':
            return menu(card)
        if score.isdigit() and int(score) in list(range(6)):
            break
    
    last_viewed = get_timestamp()

    updated_card = Card(
        card.front, 
        card.back, 
        score, 
        last_viewed
    )

    return updated_card
