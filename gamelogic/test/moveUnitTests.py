from gamelogic.balls import BallColors
from gamelogic.board import FieldState
from gamelogic.game import Game
from gamelogic.moves import Placement, Capture

__author__ = 'tomek'

import unittest

class PlacementTest(unittest.TestCase):
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

    def test_fromString(self):
        m = Placement.fromString("Wd1")
        m = Placement.fromString("Wd1,e2")
        self.assertIsNone(Placement.fromString("dupa"))
        self.assertIsNone(Placement.fromString("W"))
        self.assertIsNone(Placement.fromString("Wa1,"))


class CaptureTest(unittest.TestCase):
    def test_SingleCapture(self):
        game = Game()
        m1 = Placement(BallColors.BLACK, "a1", "a2")
        m1.execute(game)
        m2 = Placement(BallColors.GRAY, "b1", "a3")
        m2.execute(game)
        m3 = Capture(["a1", "c1"])
        m3.execute(game)
        #TODO: do sprawdzenia stan pol i liczba kulek u graczy

    def test_SingleCaptureNotValidToNonEmptyField(self):
        game = Game()
        Placement(BallColors.BLACK, "a1", "a2").execute(game)
        Placement(BallColors.GRAY, "b1", "c1").execute(game)
        m3 = Capture(["a1", "c1"])
        res = m3.validate(game)
        self.assertFalse(res[0])

    def test_SingleCaptureNotValidWithEmptyMiddle(self):
        game = Game()
        Placement(BallColors.BLACK, "a1", "a2").execute(game)
        m2 = Capture(["a1", "c1"])
        res = m2.validate(game)
        self.assertFalse(res[0])

    def test_MultiCapture(self):
        game = Game()
        Placement(BallColors.BLACK, "a1", "a2").execute(game)
        Placement(BallColors.GRAY, "b1", "g4").execute(game)
        Placement(BallColors.GRAY, "d2", "e6").execute(game)
        self.assertTrue(Capture(["a1", "c1", "e2"]).validate(game)[0])
        res = Capture(["a1", "c1", "e2"]).execute(game)
        self.assertTrue(res[0])


if __name__ == '__main__':
    unittest.main()
