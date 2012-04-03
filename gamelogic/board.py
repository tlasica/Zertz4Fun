from gamelogic.balls import BallColors

__author__ = 'tlasica'

class FieldState:
    EMPTY = "O"
    REMOVED = "x"
    WHITE = BallColors.WHITE
    GRAY = BallColors.GRAY
    BLACK = BallColors.BLACK


class BoardSize:
    ROW_SIZES = {"a":4, "b":5, "c":6, "d":7, "e":6, "f":5, "g":4}
    ROW_NAMES = ["a","b","c","d","e","f","g"]

    @staticmethod
    def rowSize(row):
        return BoardSize.ROW_SIZES[row]

    @staticmethod
    def getRowNames():
        return BoardSize.ROW_NAMES

class Board:
    """
    Board respects only state of the board (balls containers excluded)
    """

    def __init__(self):
        self.board = {}
        pass

    def putBall(self, coord, ball):
        assert self.board[coord] == FieldState.EMPTY
        self.board[coord] = ball

    def removePiece(self, coord):
        assert self.board[coord] <> FieldState.REMOVED
        res = self.board[coord]
        self.board[coord] = FieldState.REMOVED
        return res

    def moveBall(self, fromCoord, toCoord):
        assert self.board[toCoord] == FieldState.EMPTY
        assert self.board[fromCoord] <> FieldState.EMPTY
        assert self.board[fromCoord] <> FieldState.REMOVED
        self.board[toCoord] = self.board[fromCoord]
        self.board[fromCoord] = FieldState.EMPTY

    def getState(self, coord):
        return self.board[coord]

    @classmethod
    def createEmptyBoard37(cls):
        res = Board()
        for i in range(1,5):
            res.board[ "a"+str(i) ] = FieldState.EMPTY
            res.board[ "g"+str(i) ] = FieldState.EMPTY
        for i in range(1,6):
            res.board[ "b%d" % i ] = FieldState.EMPTY
            res.board[ "f"+str(i) ] = FieldState.EMPTY
        for i in range(1,7):
            res.board[ "c"+str(i) ] = FieldState.EMPTY
            res.board[ "e"+str(i) ] = FieldState.EMPTY
        for i in range(1,8):
            res.board[ "d"+str(i) ] = FieldState.EMPTY
        return res


#To check if one can isolate a piece it is required to check that
#any 2 sequential pieces from surrounding ring are removed
#e.g. for B4 a surrounding ring is [a4,b5,c4,c3,b3,a3]


class IsolatingHelper:

    def __init__(self):
        self.outerRing = {"a1", "a2", "a3", "a4"}
        self.outerRing |= {"b5","c6","d7","e6","f5"}
        self.outerRing |= {"g4", "g3", "g2", "g1"}
        self.outerRing |= {"b1", "c1", "d1", "e1", "f1"}

        self.surroundings = {}
        for row in BoardSize.getRowNames():
            for num in xrange(1, BoardSize.rowSize(row)+1):
                coord = row+str(num)
                if not coord in self.outerRing:
                    coordRing = self.__buildRing(row, num)
                    self.surroundings[ coord ] = coordRing

    def coordCanBeAlwaysRemoved(self, coord):
        return coord in self.outerRing

    def getSurrounding(self, coord):
        return self.surroundings[coord]


    def __buildRing(self, row, num):
        nextRow = chr(ord(row)+1)
        prevRow = chr(ord(row)-1)
        ring = []
        ring.append( "%s%d" % (row, num+1) )
        ring.append( "%s%d" % (nextRow, num) )
        ring.append( "%s%d" % (nextRow, num-1) )
        ring.append( "%s%d" % (row, num-1) )
        ring.append( "%s%d" % (prevRow, num-1) )
        ring.append( "%s%d" % (prevRow, num) )
        return ring