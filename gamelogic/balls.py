__author__ = 'tlasica'

class BallColors:
    WHITE = "W"
    GRAY = "G"
    BLACK = "B"


class BallContainer:
    """Container for marbles(balls): White, Gray and Black"""
    def __init__(self):
        self.balls = {BallColors.WHITE: 0, BallColors.GRAY: 0, BallColors.BLACK: 0}

    def add(self, ballColor, ballCount):
        currCount = self.balls[ballColor]
        newCount = currCount + ballCount
        self.balls[ballColor] = newCount
        return newCount

    def removeOne(self, ballColor):
        currCount = self.balls[ballColor]
        assert currCount > 0
        newCount = currCount - 1
        self.balls[ballColor] = newCount
        return newCount

    def get(self, ballColor):
        return self.balls[ballColor]


