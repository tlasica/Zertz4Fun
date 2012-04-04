__author__ = 'tomek'

class Placement:
    def __self(self, ballColor, placeCoord, removeCoord):
        self.ball = ballColor
        self.placeCoord = placeCoord
        self.removeCoord = removeCoord

    def validate(self, game):
        # target field is empty
        board = game.getBoard()
        if not board.isEmpty(self.placeCoord):
            return False, "target field %s is not EMPTY" % self.placeCoord
            # there is enough balls in left or player balls
        gameBalls = game.getRemainingBalls()
        if not gameBalls.get(self.ball) and not game.getCurrentPlayerBalls().get(self.ball):
            return False, "not enough balls of %s" % self.ball
        if self.removeCoord:
            # removed field is empty
            if not board.isEmpty(self.removeCoord):
                return False, "field %s cannot be removed - it is not empty" % self.removeCoord
                # removed field is free (can be isolated)
            if not board.canBeIsolated(self.removeCoord):
                return False, "field %s cannot be removed - it is not free" % self.removeCoord
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


class Capture:
    pass


class Isolation:
    pass