from random import random
import card_repository

def pick_card(conn, cursor):

    card = None

    while card == None:
        random_float = random()

        if random_float < 0.4:
            score = 0
        elif random_float < 0.7:
            score = 1
        elif random_float < 0.85:
            score = 2
        elif random_float < 0.95:
            score = 3
        elif random_float < 0.985:
            score = 4
        else:
            score = 5

        card = card_repository.get_random(cursor, score)

    return card
