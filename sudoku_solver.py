# sudoku_solver.py

from sudoku_board import SudokuBoard
from typing import List, Tuple, Optional


class BoardBase:
    def save_to_file(self, filename: str):
        raise NotImplementedError

    def load_from_file(self, filename: str):
        raise NotImplementedError

class SudokuBoard(BoardBase):
    def __init__(self, board: Optional[List[List[int]]] = None):
        if board:
            self.board = board
        else:
            self.board = [[0 for _ in range(9)] for _ in range(9)]

    def save_to_file(self, filename: str):
        with open(filename, 'w') as f:
            for row in self.board:
                f.write(' '.join(str(num) for num in row) + '\n')

    def load_from_file(self, filename: str):
        with open(filename, 'r') as f:
            self.board = [list(map(int, line.strip().split())) for line in f.readlines()]

    def print_board(self):
        for row in self.board:
            print(' '.join(str(num) for num in row))

class SudokuSolver:
    _instance = None

    def __init__(self, board: SudokuBoard):
        self.board = board

    @classmethod
    def get_instance(cls, board: SudokuBoard):
        if cls._instance is None:
            cls._instance = SudokuSolver(board)
        return cls._instance

    def is_valid(self, row: int, col: int, num: int) -> bool:
        for i in range(9):
            if self.board.board[row][i] == num or self.board.board[i][col] == num:
                return False

        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(3):
            for j in range(3):
                if self.board.board[start_row + i][start_col + j] == num:
                    return False

        return True

    def find_empty(self) -> Optional[Tuple[int, int]]:
        for i in range(9):
            for j in range(9):
                if self.board.board[i][j] == 0:
                    return (i, j)
        return None

    def solve(self) -> bool:
        empty = self.find_empty()
        if not empty:
            return True
        row, col = empty

        for num in range(1, 10):
            if self.is_valid(row, col, num):
                self.board.board[row][col] = num

                if self.solve():
                    return True

                self.board.board[row][col] = 0

        return False


if __name__ == "__main__":
    board = SudokuBoard()
    board.board = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]

    solver = SudokuSolver.get_instance(board)
    if solver.solve():
        print("Sudoku solved successfully!")
        board.print_board()
        board.save_to_file("solved_sudoku.txt")
    else:
        print("No solution exists.")