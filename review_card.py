from getpass import getpass
from card import Card
from get_timestamp import get_timestamp

def review_card(card):
    
    print(card.front)
    getpass('[Enter to flip the card.]')
    print(card.back)

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
