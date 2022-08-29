import puzzles
import math
import random
from SudokuSolver import SudokuSolver

if __name__ == "__main__":
    # Gives a random puzzle from puzzles to solve
    puzzle = SudokuSolver(puzzles.puzzles[math.floor(
        random.random() * len(puzzles.puzzles))])

    print("Unsolved Sudoku Puzzle")
    print(puzzle)
    puzzle.solve()
    print("Solved Sudoku Puzzle")
    print(puzzle)
