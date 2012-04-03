from gamelogic.board import FieldState

__author__ = 'tomek'

class PlaceBall:
    def __self(self, ballColor, placeCoord, removeCoord):
        self.ball = ballColor
        self.placeCoord = placeCoord
        self.removeCoord = removeCoord

    def validate(self, game):
        # target field is empty
        board = game.getBoard()
        if board.getState(self.placeCoord) != FieldState.EMPTY:
            return False, "target field %s is not EMPTY" % self.placeCoord
            # there is enough balls in left or player balls
        gameBalls = game.getRemainingBalls()
        if not gameBalls.get(self.ball):
            if not game.getCurrentPlayerBalls().get(self.ball):
                return False, "not enough balls of %s" % self.ball
        if self.removeCoord:
            # removed field is empty
            if board.getState(self.removeCoord) != FieldState.EMPTY:
                return False, "removed field %s is not empty" % self.removeCoord
                # removed field is free (can be isolated)
                #TODO: implement this check with another class
        return True, "move is valid"

    def execute(self, game):
        board = game.getBoard()
        board.putBall(self.placeCoord, self.ball)
        gameBalls = game.getRemainingBalls()
        if gameBalls.get(self.ball) > 0:
            gameBalls.removeOne(self.ball)
        else:
            game.getCurrentPlayerBalls().removeOne(self.ball)
        if self.removeCoord:
            board.removePiece(self.removeCoord)


    def __str__(self):
        """
        Returns string with ball, place coord and remove coordinates e.g. Wd1,d4
        If no piece is removed returns form of Wd1 instead.
        """
        if self.removeCoord:
            return '%s%s' % (self.ball, self.placeCoord)
        else:
            return '%s%s,%s' % (self.ball, self.placeCoord, self.removeCoord)
        pass


class CaptureBalls:
    pass


class IsolateBalls:
    pass