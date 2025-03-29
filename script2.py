import pygame
from tkinter import filedialog
import time

def load_sudoku():
    """Loads a Sudoku grid from a text file chosen by the user."""
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if not file_path:
        return None  # No file selected
    
    grid = []
    with open(file_path, "r") as file:
        for line in file:
            grid.append([int(c) if c.isdigit() else 0 for c in line.strip()])
    
    return grid

class SudokuSolver:
    def __init__(self, grid):
        self.grid = grid
    
    def is_valid(self, row, col, num):
        for i in range(9):
            if self.grid[row][i] == num or self.grid[i][col] == num:
                return False
        
        start_row, start_col = (row // 3) * 3, (col // 3) * 3
        for i in range(3):
            for j in range(3):
                if self.grid[start_row + i][start_col + j] == num:
                    return False
        return True
    
    def solve_backtracking(self):
        for row in range(9):
            for col in range(9):
                if self.grid[row][col] == 0:
                    for num in range(1, 10):
                        if self.is_valid(row, col, num):
                            self.grid[row][col] = num
                            if self.solve_backtracking():
                                return True
                            self.grid[row][col] = 0
                    return False
        return True
    
    def solve_bruteforce(self):
        """Brute-force approach testing every number with a 1-minute timeout."""
        empty_cells = [(r, c) for r in range(9) for c in range(9) if self.grid[r][c] == 0]
        start_time = time.time()
        
        def backtrack(index):
            if time.time() - start_time > 60:  # Stop after 1 minute
                return False
            if index == len(empty_cells):
                return True
            
            row, col = empty_cells[index]
            for num in range(1, 10):
                if self.is_valid(row, col, num):
                    self.grid[row][col] = num
                    if backtrack(index + 1):
                        return True
                    self.grid[row][col] = 0
            return False
        
        return backtrack(0)

def draw_grid(screen, grid, time_text):
    screen.fill((255, 255, 255))
    font = pygame.font.Font(None, 36)
    for i in range(9):
        for j in range(9):
            rect = pygame.Rect(j * 50, i * 50, 50, 50)
            pygame.draw.rect(screen, (0, 0, 0), rect, 1)
            num = grid[i][j]
            if num != 0:
                text = font.render(str(num), True, (0, 0, 0))
                screen.blit(text, (j * 50 + 15, i * 50 + 10))
    
    time_font = pygame.font.Font(None, 28)
    screen.blit(time_font.render(time_text, True, (0, 0, 0)), (20, 600))

def draw_buttons(screen, button_rects):
    font = pygame.font.Font(None, 28)
    buttons = ["Load", "Clear", "Backtrack", "Brute Force"]
    for i, text in enumerate(buttons):
        pygame.draw.rect(screen, (200, 200, 200), button_rects[i])
        pygame.draw.rect(screen, (0, 0, 0), button_rects[i], 2)
        screen.blit(font.render(text, True, (0, 0, 0)), (button_rects[i].x + 10, button_rects[i].y + 5))

def main():
    pygame.init()
    screen = pygame.display.set_mode((450, 650))
    pygame.display.set_caption("Sudoku Solver")
    clock = pygame.time.Clock()
    grid = [[0] * 9 for _ in range(9)]
    time_text = ""
    
    button_rects = [pygame.Rect(20, 460 + i * 40, 150, 30) for i in range(4)]
    
    running = True
    while running:
        screen.fill((255, 255, 255))
        draw_grid(screen, grid, time_text)
        draw_buttons(screen, button_rects)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if button_rects[0].collidepoint(x, y):
                    new_grid = load_sudoku()
                    if new_grid:
                        grid = new_grid
                        time_text = ""
                elif button_rects[1].collidepoint(x, y):
                    grid = [[0] * 9 for _ in range(9)]
                    time_text = ""
                elif button_rects[2].collidepoint(x, y):
                    solver = SudokuSolver(grid)
                    start_time = time.time()
                    solver.solve_backtracking()
                    elapsed_time = time.time() - start_time
                    time_text = f"Backtracking: {elapsed_time:.4f} sec"
                elif button_rects[3].collidepoint(x, y):
                    solver = SudokuSolver(grid)
                    start_time = time.time()
                    solver.solve_bruteforce()
                    elapsed_time = time.time() - start_time
                    time_text = f"Brute-force: {elapsed_time:.4f} sec (max 60 sec)"
        
        pygame.display.flip()
        clock.tick(30)
    
    pygame.quit()

if __name__ == "__main__":
    main()
