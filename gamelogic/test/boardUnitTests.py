from gamelogic.balls import BallColors
from gamelogic.board import FieldState, Board, BoardSize, IsolatingHelper, CaptureHelper

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
        b.putBall("b1", BallColors.BLACK)
        self.assertEquals(FieldState.BLACK, b.getState("a1"))
        x = b.removePiece("a2")
        self.assertEquals(FieldState.BLACK, b.getState("a1"))
        self.assertEquals(FieldState.REMOVED, b.getState("a2"))
        self.assertEquals(FieldState.EMPTY, x)
        b.captureOneBall("a1", "c1")
        self.assertEquals(FieldState.EMPTY, b.getState("a1"))
        self.assertEquals(FieldState.BLACK, b.getState("c1"))
        self.assertEquals(FieldState.EMPTY, b.getState("b2"))    # no side effect
        self.assertEquals(FieldState.REMOVED, b.getState("a2"))    # no side effect


class BoardSizeTest(unittest.TestCase):
    def test_rowSizes(self):
        self.assertEquals(4, BoardSize.rowSize("a"))
        self.assertEquals(7, BoardSize.rowSize("d"))
        self.assertEquals(6, BoardSize.rowSize("e"))


class CaptureHelperTest(unittest.TestCase):
    def test_getCapturedCoord(self):
        self.assertEquals("a2", CaptureHelper.getCapturedCoord("a1", "a3"))
        self.assertEquals("a2", CaptureHelper.getCapturedCoord("a3", "a1"))
        self.assertEquals("b1", CaptureHelper.getCapturedCoord("a1", "c1"))
        self.assertEquals("b1", CaptureHelper.getCapturedCoord("c1", "a1"))
        self.assertEquals("b5", CaptureHelper.getCapturedCoord("a4", "c6"))
        self.assertEquals("b5", CaptureHelper.getCapturedCoord("c6", "a4"))
        self.assertEquals("d2", CaptureHelper.getCapturedCoord("c1", "e2"))
        self.assertEquals("d2", CaptureHelper.getCapturedCoord("e2", "c1"))
        self.assertIsNone(CaptureHelper.getCapturedCoord("a1", "a4"))
        self.assertIsNone(CaptureHelper.getCapturedCoord("c2", "e6"))


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

    def test_CaptureHelper(self):
        self.assertEquals(CaptureHelper.getCapturedCoord("a1", "a3"), "a2")
        self.assertEquals(CaptureHelper.getCapturedCoord("b5", "b3"), "b4")
        self.assertEquals(CaptureHelper.getCapturedCoord("c3", "e3"), "d3")
        self.assertEquals(CaptureHelper.getCapturedCoord("c3", "a3"), "b3")

if __name__ == '__main__':
    unittest.main()
