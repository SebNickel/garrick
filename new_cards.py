import card_repository
from new_card import new_card

def new_cards(conn, cursor, two_way_card, single_line_mode):

    while True:

        card, two_way_card, single_line_mode = \
            new_card(conn, cursor, two_way_card, single_line_mode)

        if card == None:
            break

        card_repository.insert(conn, cursor, card)

        if two_way_card:

            flipped_card = Card(
                card.back,
                card.front,
                card.score,
                card.last_viewed
            )

            card_repository.insert(conn, cursor, flipped_card)
