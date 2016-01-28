from new_card import new_card

def new_cards(conn, cursor, two_way_card):
    while True:
        two_way_card = new_card(conn, cursor, two_way_card)
        if two_way_card == None:
            break
