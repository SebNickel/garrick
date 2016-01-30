from getpass import getpass
from card import Card
from unescape import unescape
from get_timestamp import get_timestamp

def review_card(card):
    
    front = unescape(card.front)
    back = unescape(card.back)

    print(front)
    getpass('[Enter to flip the card.]')
    print(back)

    while True:
        score = input('Score yourself from 0 to 5: ')
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
