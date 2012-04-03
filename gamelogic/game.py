from gamelogic.balls import BallContainer, BallColors
from gamelogic.board import Board

__author__ = 'tomek'

class Players:
    PLY1 = "ply1"
    PLY2 = "ply2"


class Game:
    """
    Game state, including board, balls and who is going to make the move now.
    """

    def __init__(self):
        self.board = Board.createEmptyBoard37() # TODO maybe factory method instead of @classmethod ?
        self.balls = BallContainer()
        self.balls.add(BallColors.WHITE, 6)
        self.balls.add(BallColors.GRAY, 8)
        self.balls.add(BallColors.BLACK, 10)
        self.players = {Players.PLY1: BallContainer(), Players.PLY2: BallContainer()}
        self.currPlayer = Players.PLY1

    def getPlayer(self, ply):
        return self.players[ply]

    def getBoard(self):
        return self.board

    def getCurrentPlayerName(self):
        return self.currPlayer

    def getRemainingBalls(self):
        return self.balls

    def nextPlayer(self):
        if self.currPlayer == Players.PLY1:
            self.currPlayer = Players.PLY2
        else:
            self.currPlayer = Players.PLY1
        return self.currPlayer

    def getCurrentPlayerBalls(self):
        return self.players[ self.currPlayer ]