import random

def load_sudoku(filename):
    """Loads a Sudoku grid from a text file."""
    grid = []
    with open(filename, "r") as file:
        for line in file:
            grid.append([int(c) if c.isdigit() else 0 for c in line.strip()])
    return grid

def get_random_sudoku_file():
    """Selects a random Sudoku file from examples folder."""
    examples = ["examples/sudoku.txt", "examples/sudoku2.txt", "examples/sudoku3.txt", "examples/sudoku4.txt", "examples/evilsudoku.txt"]
    return random.choice(examples)
