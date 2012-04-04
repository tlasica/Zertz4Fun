from gamelogic.balls import BallColors
from gamelogic.board import FieldState, Board, BoardSize, IsolatingHelper

__author__ = 'tomek'

import unittest

class BoardTest(unittest.TestCase):
    def test_createEmptyBoard(self):
        b = Board.createEmptyBoard37()
        self.assertIsNotNone(b)
        self.assertEquals(FieldState.EMPTY, b.getState("a4"))
        self.assertEquals(FieldState.EMPTY, b.getState("b5"))
        self.assertEquals(FieldState.EMPTY, b.getState("c6"))
        self.assertEquals(FieldState.EMPTY, b.getState("d7"))
        self.assertEquals(FieldState.EMPTY, b.getState("e6"))
        self.assertEquals(FieldState.EMPTY, b.getState("f5"))
        self.assertEquals(FieldState.EMPTY, b.getState("g4"))

    def test_simpleActions(self):
        b = Board.createEmptyBoard37()
        b.putBall("a1", BallColors.BLACK)
        self.assertEquals(FieldState.BLACK, b.getState("a1"))
        x = b.removePiece("a2")
        self.assertEquals(FieldState.BLACK, b.getState("a1"))
        self.assertEquals(FieldState.REMOVED, b.getState("a2"))
        self.assertEquals(FieldState.EMPTY, x)
        b.moveBall("a1", "c3")
        self.assertEquals(FieldState.EMPTY, b.getState("a1"))
        self.assertEquals(FieldState.BLACK, b.getState("c3"))
        self.assertEquals(FieldState.EMPTY, b.getState("b2"))    # no side effect
        self.assertEquals(FieldState.REMOVED, b.getState("a2"))    # no side effect


class BoardSizeTest(unittest.TestCase):
    def test_rowSizes(self):
        self.assertEquals(4, BoardSize.rowSize("a"))
        self.assertEquals(7, BoardSize.rowSize("d"))
        self.assertEquals(6, BoardSize.rowSize("e"))


class IsolatingHeperTest(unittest.TestCase):
    def test_outerRing(self):
        iso = IsolatingHelper()
        self.assertTrue(iso.canAlwaysRemove("a1"))
        self.assertTrue(iso.canAlwaysRemove("a4"))
        self.assertTrue(iso.canAlwaysRemove("b5"))
        self.assertTrue(iso.canAlwaysRemove("d7"))
        self.assertTrue(iso.canAlwaysRemove("g2"))
        self.assertTrue(iso.canAlwaysRemove("e1"))
        self.assertFalse(iso.canAlwaysRemove("b2"))
        self.assertFalse(iso.canAlwaysRemove("d5"))
        self.assertFalse(iso.canAlwaysRemove("f4"))

    def test_surroundings(self):
        iso = IsolatingHelper()
        surr = iso.getNeighbours("b2")
        self.assertEquals(surr, ["b3", "c2", "c1", "b1", "a1", "a2"])

if __name__ == '__main__':
    unittest.main()
