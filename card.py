class Card:
    def __init__(self, front, back, score, last_viewed):
        self.front = front
        self.back = back
        self.score = score
        self.last_viewed = last_viewed
    def to_tuple(self):
        return (
            self.front,
            self.back,
            self.score,
            self.last_viewed
        )
