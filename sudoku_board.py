# sudoku_board.py

import random

class SudokuBoard:
    def __init__(self, board=None):
        if board is None:
            self.board = [[0] * 9 for _ in range(9)]
        else:
            self.board = board
        self.solved_board = [[0] * 9 for _ in range(9)]
        self.solved = False

    def is_valid(self, row, col, num):
        for j in range(9):
            if self.board[row][j] == num:
                return False

        for i in range(9):
            if self.board[i][col] == num:
                return False

        box_row = (row // 3) * 3
        box_col = (col // 3) * 3
        for i in range(box_row, box_row + 3):
            for j in range(box_col, box_col + 3):
                if self.board[i][j] == num:
                    return False

        return True

    def print_board(self):
        for i in range(9):
            row = " ".join(str(num) if num != 0 else "." for num in self.board[i])
            print(row)

    def load_board(self, board):
        self.board = board

    def export_board(self):
        return self.board