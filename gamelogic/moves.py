from gamelogic.board import CaptureHelper

__author__ = 'tomek'

'''
A. Placing a marble and removing a ring.
First note down the colour of the marble you choose to play with and the coordinate of the ring you put it onto. Next you put a comma, followed by the coordinate of the ring you remove.
For example: Wd4,d1
B. Capturing one or more marbles by jumping.
A capture must be marked with a small "x". That you note down first. Next you write down the coordinate of the ring with the marble you'll use to capture, followed by the letter that indicates the colour of the marble you capture, and next the coordinate of the ring where your move ends. If you can make a second capture, you go on with the letter of the second marble you jump over, followed by the coordinate of the ring where the marble lands, etc.
For example: x d1Gd3Wd5
C. Capturing one or more marbles by isolating.
Note down your move as described in A. above. If the ring you remove isolates one or more marbles, then you mark it with a small "x", followed by the colour(s) of the marble(s) you isolate and the coordinate(s) of the ring(s).
For example: Bd7,b2 x Wa1Wa2
'''

class Placement:
    """
    Placement move mandatory puts a new ball on the board.
    Optionally it can remove a piece.
    Removed piece can create an isolated island.
    """

    def __init__(self, ballColor, placeCoord, removeCoord):
        self.ball = ballColor
        self.placeCoord = placeCoord
        self.removeCoord = removeCoord

    def validate(self, game):
        """
        Validates if placement can be done according to current board and ballsets status
        as if the move is performed by current player.
        """
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
            #TODO: isolation


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

    def __init__(self, coordList):
        self.coordList = coordList
        assert len(coordList) >= 2

    def validate(self, game):
        board = game.getBoard()
        #non-empty start coord
        startCoord = self.coordList[0]
        if not board.isBall(startCoord):
            return False, "%s should be occupied with a ball" % startCoord
        # each next should be empty and there should be a ball captured
        fromCoord = self.coordList[0]
        for toCoord in self.coordList[1:]:
            captureCoord = CaptureHelper.getCapturedCoord(fromCoord, toCoord)
            if not board.isEmpty(toCoord):
                return False, "%s should be empty" % toCoord
            if not board.isBall(captureCoord):
                return False, "%s should be occupied" % captureCoord
            # next
            fromCoord = toCoord
        return True, "move is valid"

    def execute(self, game):
        """
        executes move of capturing (strikes) including changing currentPly ball set
        """
        capturedBalls = []
        board = game.getBoard()
        fromCoord = self.coordList[0]
        for toCoord in self.coordList[1:]:
            capture = board.captureOneBall(fromCoord, toCoord)
            capturedBalls.append( capture )
            game.getCurrentPlayerBalls().add(capture[1], 1)
            fromCoord = toCoord # next part of move
        return capturedBalls

class StringToMoveConverter:
    """
    Converts string to a Placement/Capture Object
    """

    def parse(self, moveStr):
        return None

