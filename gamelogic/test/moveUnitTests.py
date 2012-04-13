from gamelogic.balls import BallColors
from gamelogic.board import FieldState
from gamelogic.game import Game
from gamelogic.moves import Placement, Capture

__author__ = 'tomek'

import unittest

class MoveTest(unittest.TestCase):
    def test_simplePlacementWithRemoval(self):
        game = Game()
        board = game.getBoard()
        self.assertEquals(FieldState.EMPTY, board.getState("a1"))
        self.assertEquals(FieldState.EMPTY, board.getState("a2"))
        m1 = Placement(BallColors.BLACK, "a1", "a2")
        m1.execute(game)
        self.assertEquals(FieldState.BLACK, board.getState("a1"))
        self.assertEquals(FieldState.REMOVED, board.getState("a2"))

    def test_simplePlacementWithNoRemoval(self):
        game = Game()
        board = game.getBoard()
        self.assertEquals(FieldState.EMPTY, board.getState("a1"))
        self.assertEquals(FieldState.EMPTY, board.getState("a2"))
        m1 = Placement(BallColors.BLACK, "a1", None)
        m1.execute(game)
        self.assertEquals(FieldState.BLACK, board.getState("a1"))
        self.assertEquals(FieldState.EMPTY, board.getState("a2"))

    def test_validatePlacementOnNonEmptyField(self):
        game = Game()
        board = game.getBoard()
        self.assertEquals(FieldState.EMPTY, board.getState("a1"))
        self.assertEquals(FieldState.EMPTY, board.getState("a2"))
        m1 = Placement(BallColors.BLACK, "a1", "a2")
        m1.execute(game)
        self.assertEquals(FieldState.BLACK, board.getState("a1"))
        self.assertEquals(FieldState.REMOVED, board.getState("a2"))
        self.assertFalse(m1.validate(game)[0])

    def test_validatePlacementNonIsolable(self):
        game = Game()
        board = game.getBoard()
        self.assertEquals(FieldState.EMPTY, board.getState("a1"))
        self.assertEquals(FieldState.EMPTY, board.getState("b2"))
        m1 = Placement(BallColors.BLACK, "a1", "b2")
        self.assertFalse(m1.validate(game)[0])

    def test_SingleCaptureI(self):
        game = Game()
        m1 = Placement(BallColors.BLACK,"a1","a2")
        m1.execute(game)
        m2 = Placement(BallColors.GRAY,"b1","a3")
        m2.execute(game)
        m3 = Capture(["a1","c1"])
        m3.execute(game)



if __name__ == '__main__':
    unittest.main()
