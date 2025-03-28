import os
import random

# Avaible files
sudoku_files = [
    "sudoku.txt",
    "sudoku2.txt",
    "sudoku3.txt",
    "sudoku4.txt",
    "evilsudoku.txt"
]

# Random selecction of sudoku files
selected_file = random.choice(sudoku_files)
file_path = os.path.join(os.path.dirname(__file__), selected_file)

# Upload the files
def load_sudoku(filename):
    """Loads a Sudoku grid from a file."""
    grid = []
    with open(filename, "r") as file:
        for line in file:
            row = [int(char) if char.isdigit() else 0 for char in line.strip()]
            grid.append(row)
    return grid

# Display the files
def print_sudoku(grid):
    """Prints the Sudoku grid in a readable format."""
    for i, row in enumerate(grid):
        if i % 3 == 0 and i != 0:
            print("-" * 21)  # Séparateurs des blocs 3x3
        print(" ".join(str(num) if num != 0 else "." for num in row))

# Upload and display the grid
print(f"📂 Fichier sélectionné : {selected_file}")
sudoku_grid = load_sudoku(file_path)
print_sudoku(sudoku_grid)
