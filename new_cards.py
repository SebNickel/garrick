from new_card import new_card

def new_cards(conn, cursor, two_way_card):
    while two_way_card != None:
        two_way_card = new_card(conn, cursor, two_way_card)
