from card import Card

def insert (conn, cursor, card):

    args = card.to_tuple()

    query = """
        INSERT INTO cards (front, back, score, last_viewed)
        VALUES ({!r}, {!r}, {}, {!r})
    """.format(*args)
    
    cursor.execute(query)
    conn.commit()

def get_random(conn, cursor, score):

    query = """
        SELECT *
        FROM cards
        WHERE score = {}
        ORDER BY RAND()
        LIMIT 1
    """.format(score)

    cursor.execute(query)
    row = cursor.fetchone()

    if row == None:
        return None
    else:
        card = Card(*row)
        return card

def update(conn, cursor, card):

    args = card.to_tuple()

    query = """
        UPDATE cards
        SET score = {2},
            last_viewed = {3!r}
        WHERE front = {0!r}
        AND back = {1!r}
    """.format(*args)

    cursor.execute(query)
    conn.commit()
