from gamelogic.balls import BallColors

__author__ = 'tlasica'

class FieldState:
    EMPTY = "O"
    REMOVED = "x"
    WHITE = BallColors.WHITE
    GRAY = BallColors.GRAY
    BLACK = BallColors.BLACK


class BoardSize:
    ROW_SIZES = {"a": 4, "b": 5, "c": 6, "d": 7, "e": 6, "f": 5, "g": 4}
    ROW_NAMES = ["a", "b", "c", "d", "e", "f", "g"]

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

    def isRemoved(self, coord):
        return self.getState(coord) == FieldState.REMOVED

    def isEmpty(self, coord):
        return self.getState(coord) == FieldState.EMPTY

    def canBeIsolated(self, coord):
        helper = IsolatingHelper.getHelper()
        if helper.canAlwaysRemove(coord):
            return True
        else:
            neighbours = helper.getNeighbours(coord)
            for i in xrange(0, 6):
                n1 = neighbours[i % 6]
                n2 = neighbours[(i + 1) % 6]
                if self.isRemoved(n1) and self.isRemoved(n2):
                    return True
            return False

    @classmethod
    def createEmptyBoard37(cls):
        res = Board()
        for i in range(1, 5):
            res.board["a" + str(i)] = FieldState.EMPTY
            res.board["g" + str(i)] = FieldState.EMPTY
        for i in range(1, 6):
            res.board["b%d" % i] = FieldState.EMPTY
            res.board["f" + str(i)] = FieldState.EMPTY
        for i in range(1, 7):
            res.board["c" + str(i)] = FieldState.EMPTY
            res.board["e" + str(i)] = FieldState.EMPTY
        for i in range(1, 8):
            res.board["d" + str(i)] = FieldState.EMPTY
        return res


#To check if one can isolate a piece it is required to check that
#any 2 sequential pieces from surrounding ring are removed
#e.g. for B4 a surrounding ring is [a4,b5,c4,c3,b3,a3]

#TODO maybe it should not be a singleton or implementation is different
class IsolatingHelper:
    INSTANCE = IsolatingHelper()

    @staticmethod
    def getHelper():
        return IsolatingHelper.INSTANCE

    def __init__(self):
        self.outerRing = {"a1", "a2", "a3", "a4"}
        self.outerRing |= {"b5", "c6", "d7", "e6", "f5"}
        self.outerRing |= {"g4", "g3", "g2", "g1"}
        self.outerRing |= {"b1", "c1", "d1", "e1", "f1"}

        self.neighbours = {}
        for row in BoardSize.getRowNames():
            for num in xrange(1, BoardSize.rowSize(row) + 1):
                coord = row + str(num)
                if not coord in self.outerRing:
                    nRing = self.__calculateNeighbours(row, num)
                    self.neighbours[coord] = nRing

    def canAlwaysRemove(self, coord):
        return coord in self.outerRing

    def getNeighbours(self, coord):
        return self.neighbours[coord]


    def __calculateNeighbours(self, row, num):
        nextRow = chr(ord(row) + 1)
        prevRow = chr(ord(row) - 1)
        ring = ["%s%d" % (row, num + 1), "%s%d" % (nextRow, num), "%s%d" % (nextRow, num - 1), "%s%d" % (row, num - 1),
                "%s%d" % (prevRow, num - 1), "%s%d" % (prevRow, num)]
        return ring
