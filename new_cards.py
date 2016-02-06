import card_repository
from card import Card
from new_card import new_card
from colored_output import print_info

def new_cards(conn, cursor, two_way_card, single_line_mode, editor_mode):

    while True:

        card, two_way_card, single_line_mode, editor_mode = \
            new_card(two_way_card, single_line_mode, editor_mode)

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

        print_info('Saved.')
