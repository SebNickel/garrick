from card import Card

def create_table_if_not_exists(conn, cursor):

    query = """
        CREATE TABLE IF NOT EXISTS cards (
            front TEXT NOT NULL,
            back TEXT NOT NULL,
            score INTEGER NOT NULL,
            last_viewed TIMESTAMP NOT NULL
        )
    """

    cursor.execute(query)
    conn.commit()

def check_if_empty(cursor):

    query = """
        SELECT EXISTS(
            SELECT 1
            FROM cards
        )
    """

    cursor.execute(query)
    query_result = cursor.fetchone()

    if query_result[0] == 0:
        return True
    else:
        return False

def insert(conn, cursor, card):

    args = card.to_tuple()

    query = """
        INSERT INTO cards (front, back, score, last_viewed)
        VALUES (?, ?, ?, ?)
    """
    
    cursor.execute(query, args)
    conn.commit()

def get_random(cursor, score):

    query = """
        SELECT *
        FROM cards
        WHERE score = ?
        ORDER BY last_viewed
        LIMIT 1
    """

    cursor.execute(query, str(score))
    row = cursor.fetchone()

    if row == None:
        return None
    else:
        card = Card(*row)
        return card

def replace(conn, cursor, old_card, new_card):

    args = new_card.to_tuple() + old_card.to_tuple()

    query = """
        UPDATE cards
        SET front = ?,
            back = ?,
            score = ?,
            last_viewed = ?
        WHERE front = ?
        AND back = ?
        AND score = ?
        AND last_viewed = ?
    """
    
    cursor.execute(query, args)
    conn.commit()

def delete(conn, cursor, card):

    args = card.to_tuple()

    query = """
        DELETE FROM cards
        WHERE front = ?
        AND back = ?
        AND score = ?
        AND last_viewed = ?
    """

    cursor.execute(query, args)
    conn.commit()
