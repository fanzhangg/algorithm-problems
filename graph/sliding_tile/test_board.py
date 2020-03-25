from unittest import TestCase
from graph.sliding_tile.sliding_tile import Board


class TestBoard(TestCase):
    def setUp(self):
        pass

    def test_up(self):
        board = Board([
            [1, 2, 0],
            [4, 5, 6],
            [7, 8, 3]
        ], 0, 2)
        board.up()

        self.assertEqual(board.data, [[1, 2, 6], [4, 5, 0], [7, 8, 3]])

        board.up()

        self.assertEqual(board.data, [[1, 2, 6], [4, 5, 3], [7, 8, 0]])

        isMoved = board.up()
        self.assertFalse(isMoved)

    def test_down(self):
        board = Board()
        board.down()

        self.assertEqual(board.data, [[1, 2, 3], [4, 5, 0], [7, 8, 6]])

        board.down()
        self.assertEqual(board.data, [[1, 2, 0], [4, 5, 3], [7, 8, 6]])

        board.down()

        self.assertFalse(board.down())

    def test_left(self):
        board = Board([
            [1, 2, 3],
            [0, 4, 5],
            [6, 7, 8]
        ], 1, 0)

        board.left()

        self.assertEqual(board.data, [[1, 2, 3], [4, 0, 5], [6, 7, 8]])

        board.left()
        self.assertEqual(board.data, [[1, 2, 3], [4, 5, 0], [6, 7, 8]])

        board.left()
        self.assertFalse(board.left())

    def test_right(self):
        board = Board()
        board.right()

        self.assertEqual(board.data, [[1, 2, 3], [4, 5, 6], [7, 0, 8]])

        board.right()
        self.assertEqual(board.data, [[1, 2, 3], [4, 5, 6], [0, 7, 8]])

        board.right()
        self.assertFalse(board.right())
    #
    # def test_is_win(self):
    #     self.fail()
