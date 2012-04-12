from gamelogic.balls import BallColors
from gamelogic.board import FieldState
import gamelogic.game
from gamelogic.moves import Placement

__author__ = 'tomek'

import unittest

class MoveTest(unittest.TestCase):
    def test_simplePlacementWithRemoval(self):
        game = gamelogic.game.Game()
        board = game.getBoard()
        self.assertEquals(FieldState.EMPTY, board.getState("a1"))
        self.assertEquals(FieldState.EMPTY, board.getState("a2"))
        m1 = Placement(BallColors.BLACK, "a1", "a2")
        m1.execute(game)
        self.assertEquals(FieldState.BLACK, board.getState("a1"))
        self.assertEquals(FieldState.REMOVED, board.getState("a2"))

    def test_simplePlacementWithNoRemoval(self):
        game = gamelogic.game.Game()
        board = game.getBoard()
        self.assertEquals(FieldState.EMPTY, board.getState("a1"))
        self.assertEquals(FieldState.EMPTY, board.getState("a2"))
        m1 = Placement(BallColors.BLACK, "a1", None)
        m1.execute(game)
        self.assertEquals(FieldState.BLACK, board.getState("a1"))
        self.assertEquals(FieldState.EMPTY, board.getState("a2"))

    def test_validatePlacementOnNonEmptyField(self):
        game = gamelogic.game.Game()
        board = game.getBoard()
        self.assertEquals(FieldState.EMPTY, board.getState("a1"))
        self.assertEquals(FieldState.EMPTY, board.getState("a2"))
        m1 = Placement(BallColors.BLACK, "a1", "a2")
        m1.execute(game)
        self.assertEquals(FieldState.BLACK, board.getState("a1"))
        self.assertEquals(FieldState.REMOVED, board.getState("a2"))
        self.assertFalse(m1.validate(game)[0])

    def test_validatePlacementNonIsolable(self):
        game = gamelogic.game.Game()
        board = game.getBoard()
        self.assertEquals(FieldState.EMPTY, board.getState("a1"))
        self.assertEquals(FieldState.EMPTY, board.getState("b2"))
        m1 = Placement(BallColors.BLACK, "a1", "b2")
        self.assertFalse(m1.validate(game)[0])

if __name__ == '__main__':
    unittest.main()
