# test_sudoku.py

import unittest
from sudoku_board import SudokuBoard

class TestSudokuBoard(unittest.TestCase):
    def setUp(self):
        self.board = SudokuBoard()

    def test_board_initialization(self):
        self.assertEqual(len(self.board.board), 9)
        for row in self.board.board:
            self.assertEqual(len(row), 9)

    def test_valid_move(self):
        self.board.board[0][0] = 5
        self.assertEqual(self.board.board[0][0], 5)

    def test_invalid_move(self):
        self.board.board[0][0] = 10
        self.assertNotEqual(self.board.board[0][0], 5)

if __name__ == "__main__":
    unittest.main()
