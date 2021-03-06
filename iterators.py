from card import Card
from pick_card import pick_card

def review_iterator(conn, cursor):
    card = pick_card(conn, cursor)
    while True:
        yield card
        card = pick_card(conn, cursor)

def browsing_iterator(rows):
    i = 0
    while i < len(rows):
        card = Card(*rows[i])
        yield card
        i += 1
