from getpass import getpass
from card import Card
import card_repository
from unescape import unescape
from get_timestamp import get_timestamp

def menu(card):
    
    print('e: Edit this card. (COMING SOON)')
    print('d: Delete this card.')

    while True:
        selection = input('[e/d]: ')
        if selection in ['e', 'd']:
            break

    if selection == 'e':
        print('COMING SOON!')
        return card
    elif selection == 'd':
        return None

def review_card(card):
    
    front = unescape(card.front)
    back = unescape(card.back)

    print(front)
    getpass('[Enter to flip the card.]')
    print(back)

    while True:
        score = input("Score yourself from 0 to 5, or enter 'o' for options: ")
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
