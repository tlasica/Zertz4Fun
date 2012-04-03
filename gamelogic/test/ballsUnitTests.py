from gamelogic.balls import BallContainer, BallColors

__author__ = 'tomek'

import unittest

class BallContainerTest(unittest.TestCase):
    def test_ifAddWorks(self):
        bc = BallContainer()
        bc.add(BallColors.WHITE, 1)
        self.assertEqual(bc.get(BallColors.WHITE), 1)
        bc.add(BallColors.WHITE, 2)
        self.assertEqual(bc.get(BallColors.WHITE), 3)

    def test_ifRemoveWorks(self):
        bc = BallContainer()
        bc.add(BallColors.BLACK, 5)
        bc.add(BallColors.WHITE, 2)
        bc.removeOne(BallColors.WHITE)
        self.assertEquals(bc.get(BallColors.BLACK), 5)
        self.assertEquals(bc.get(BallColors.WHITE), 1)
        bc.removeOne(BallColors.BLACK)
        self.assertEquals(bc.get(BallColors.BLACK), 4)

if __name__ == '__main__':
    unittest.main()
