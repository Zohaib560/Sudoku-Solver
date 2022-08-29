import math


class SudokuSolver:
    """
    A Sudoku Solver Class which takes in a solvable sudoku puzzle and can
    then output the solution for that puzzle. The class was initialized
    designed for 9x9 puzzles but can take in any size puzzle so long as it
    is a valid sudoku puzzle, dimensions are of a square (same size lengths),
    and sqrt(X) is int.

    Some additional board sizes that would work are 9x9, 16x16, 25x25, etc

    === Attributes ===
    board: A valid and solvable sudoku puzzle. Note: A 0 on the board represents
    a blank space.
    """

    def __init__(self, board):
        self.board = board

    def __str__(self):
        string = ""
        subgrid_size = int(math.sqrt(len(self.board)))
        for row in range(len(self.board)):
            if (row % subgrid_size == 0) and (row != 0):
                string += "- - - - - - - - - - - -\n"
            for col in range(len(self.board[0])):
                if (col % subgrid_size == 0) and (col != 0):
                    string += " | "

                if col == len(self.board[0]) - 1:
                    string += str(self.board[row][col]) + " \n"
                else:
                    string += str(self.board[row][col]) + " "
        return string

    def _find_next_empty(self):
        """
        returns a tuple of row, col which is the location of a 0 in the board
        """
        for row in range(len(self.board)):
            for col in range(len(self.board)):
                if self.board[row][col] == 0:
                    return row, col
        return None

    def _validate(self, num, pos):
        """
        returns true if placement of num at pos tuple of (row, col) in the
        sudoku board is valid (doesn't violate rules of sudoku, row, columns
        and internal grid cannot have repeating numbers) else false
        """

        # check row
        if num in self.board[pos[0]]:
            return False  # Do not add since it would be invalid

        # check col
        for entry in range(len(self.board)):
            if self.board[entry][pos[1]] == num:
                return False  # Do not add since it would be invalid

        # check x by x subgrid
        subgrid_size = int(math.sqrt(len(self.board)))
        subgrid_x = pos[1] // subgrid_size
        subgrid_y = pos[0] // subgrid_size
        for row in range(subgrid_y * subgrid_size,
                         subgrid_y * subgrid_size + subgrid_size):
            for col in range(subgrid_x * subgrid_size,
                             subgrid_x * subgrid_size + subgrid_size):
                if self.board[row][col] == num:
                    return False  # Do not add since it would be invalid

        # passed all validation and num can be inserted
        return True

    def solve(self):
        """
        recursively solves the sudoku puzzle board using a backtracking
        algorithm, it returns true if there are still blanks else false

        Simple Backtracking Algorithm
        find next available spot and pick a valid number to place, continue
        until the next spot cannot be filled by a valid number, if this happens
        then backtrack to the last number placement and try a different number.
        Continue until all spots have been filled in.
        """
        empty_space = self._find_next_empty()
        if not empty_space:
            return True
        else:
            row, col = empty_space
            for num in range(1, len(self.board) + 1):  # go through valid inputs
                if self._validate(num, (row, col)):
                    self.board[row][col] = num

                    if self.solve():
                        return True
                    self.board[row][col] = 0
            return False
