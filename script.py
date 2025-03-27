import customtkinter as ctk
from tkinter import filedialog
import numpy as np

class SudokuSolver:
    def __init__(self, grid):
        self.grid = grid
    
    def is_valid(self, row, col, num):
        # Vérifie si le nombre n'est pas dans la ligne, colonne ou le bloc 3x3
        if num in self.grid[row]:
            return False
        if num in self.grid[:, col]:
            return False
        start_row, start_col = (row // 3) * 3, (col // 3) * 3
        if num in self.grid[start_row:start_row+3, start_col:start_col+3]:
            return False
        return True
    
    def solve(self):
        for row in range(9):
            for col in range(9):
                if self.grid[row][col] == 0:
                    for num in range(1, 10):
                        if self.is_valid(row, col, num):
                            self.grid[row][col] = num
                            if self.solve():
                                return True
                            self.grid[row][col] = 0
                    return False
        return True

class SudokuApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Sudoku Solver")
        self.geometry("450x500")
        
        self.grid_values = np.zeros((9, 9), dtype=int)
        self.solver = None
        
        self.create_widgets()
    
    def create_widgets(self):
        self.cells = []
        frame = ctk.CTkFrame(self)
        frame.grid(row=0, column=0, padx=10, pady=10)
        
        for i in range(9):
            row = []
            for j in range(9):
                entry = ctk.CTkEntry(frame, width=40, height=40, justify='center', font=("Arial", 16))
                entry.grid(row=i, column=j, padx=(2 if j % 3 == 2 else 0), pady=(2 if i % 3 == 2 else 0))
                row.append(entry)
            self.cells.append(row)
        
        self.load_button = ctk.CTkButton(self, text="Charger Sudoku", command=self.load_sudoku)
        self.load_button.grid(row=1, column=0, pady=10)
        
        self.solve_button = ctk.CTkButton(self, text="Résoudre", command=self.solve_sudoku)
        self.solve_button.grid(row=2, column=0, pady=10)
    
    def load_sudoku(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        if file_path:
            with open(file_path, 'r') as file:
                lines = file.readlines()
                for i, line in enumerate(lines):
                    numbers = [int(n) if n != '_' else 0 for n in line.strip()]
                    self.grid_values[i] = numbers
                    for j, num in enumerate(numbers):
                        self.cells[i][j].delete(0, 'end')
                        if num != 0:
                            self.cells[i][j].insert(0, str(num))
        self.solver = SudokuSolver(self.grid_values)
    
    def solve_sudoku(self):
        if self.solver and self.solver.solve():
            for i in range(9):
                for j in range(9):
                    self.cells[i][j].delete(0, 'end')
                    self.cells[i][j].insert(0, str(self.solver.grid[i][j]))
        else:
            print("Aucune solution trouvée")

if __name__ == "__main__":
    app = SudokuApp()
    app.mainloop()
