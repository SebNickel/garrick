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

def select(cursor, score):

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

def select_by_regex(cursor, regex):

    query = """
        SELECT *
        FROM cards
        WHERE MATCHES(?, front)
        OR MATCHES(?, back)
    """

    cursor.execute(query, (regex, regex))

    results = cursor.fetchall()

    return results

def select_by_regex_front(cursor, regex):

    query = """
        SELECT *
        FROM cards
        WHERE MATCHES(?, front)
    """

    cursor.execute(query, (regex,))

    results = cursor.fetchall()

    return results

def select_by_regex_back(cursor, regex):

    query = """
        SELECT *
        FROM cards
        WHERE MATCHES(?, back)
    """

    cursor.execute(query, (regex,))

    results = cursor.fetchall()

    return results

def select_by_score(cursor, score):

    query = """
        SELECT *
        FROM cards
        WHERE score = ?
    """

    cursor.execute(query, (score,))

    results = cursor.fetchall()

    return results

def select_by_last_viewed(cursor):

    query = """
        SELECT *
        FROM cards
        ORDER BY last_viewed
    """

    cursor.execute(query)

    results = cursor.fetchall()

    return results

def select_by_last_viewed_reverse(cursor):

    query = """
        SELECT *
        FROM cards
        ORDER BY last_viewed DESC
    """

    cursor.execute(query)

    results = cursor.fetchall()

    return results

def update_flipped_card(conn, cursor, card, updated_card):

    args = (updated_card.back, updated_card.front, card.back, card.front)

    query = """
        UPDATE cards
        SET front = ?,
            back = ?
        WHERE front = ?
        AND back = ?
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

def delete_flipped_card(conn, cursor, card):

    args = (card.back, card.front)

    query = """
        DELETE FROM cards
        WHERE front = ?
        AND back = ?
    """

    cursor.execute(query, args)
    conn.commit()

def is_two_way_card(cursor, card):
    
    args = (card.back, card.front)

    query = """
        SELECT EXISTS(
            SELECT *
            FROM cards
            WHERE front = ?
            AND back = ?
        )
    """

    cursor.execute(query, args)
    query_result = cursor.fetchone()

    if query_result[0] == 0:
        return False
    else:
        return True

def count(cursor):
    
    query = """
        SELECT count(*)
        FROM cards
    """

    cursor.execute(query)

    result = cursor.fetchone()

    return int(result[0])
