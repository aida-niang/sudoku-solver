import pygame
import time
import random
from sudoku import Sudoku
from brute_force_solver import brute_force_solver
from backtracking_solver import backtracking_solver
from grid import load_sudoku, get_random_sudoku_file
import settings 

# Main Game Loop
def main():
    running = True
    selected_cell = None
    filename = get_random_sudoku_file()
    grid = load_sudoku(filename)
    sudoku = Sudoku(grid)
    algorithm_choice = None
    solved = False

    # Créer les boutons pour sélectionner l'algorithme
    brute_force_button = pygame.Rect(50, 550, 150, 50)
    backtracking_button = pygame.Rect(250, 550, 200, 50)

    while running:
        settings.screen.fill(settings.WHITE)
        sudoku.draw_grid(settings.screen)

        # Dessiner les boutons
        pygame.draw.rect(settings.screen, settings.GREEN, brute_force_button)
        pygame.draw.rect(settings.screen, settings.BLUE, backtracking_button)
        font = pygame.font.Font(None, 36)
        brute_force_text = font.render('Force Brute', True, settings.WHITE)
        backtracking_text = font.render('Backtracking', True, settings.WHITE)
        settings.screen.blit(brute_force_text, (brute_force_button.x + 15, brute_force_button.y + 10))
        settings.screen.blit(backtracking_text, (backtracking_button.x + 15, backtracking_button.y + 10))

        # Handle user input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                col, row = x // settings.CELL_SIZE, y // settings.CELL_SIZE
                if selected_cell == (row, col):
                    selected_cell = None
                else:
                    selected_cell = (row, col)
                # Vérifier si un bouton a été cliqué
                if brute_force_button.collidepoint(x, y):
                    algorithm_choice = "1"  # Choix de la force brute
                elif backtracking_button.collidepoint(x, y):
                    algorithm_choice = "2"  # Choix du backtracking
            if event.type == pygame.KEYDOWN:
                if selected_cell and event.key in range(pygame.K_1, pygame.K_9 + 1):
                    row, col = selected_cell
                    num = event.key - pygame.K_1 + 1
                    if sudoku.is_valid(row, col, num):
                        sudoku.grid[row][col] = num

        # Highlight selected cell
        if selected_cell:
            row, col = selected_cell
            sudoku.highlight_cell(row, col, settings.screen)

        # Résoudre le Sudoku si un algorithme est sélectionné
        if algorithm_choice:
            start_time = time.time()
            if algorithm_choice == "1":  # Force brute
                solved = brute_force_solver(sudoku)
            elif algorithm_choice == "2":  # Backtracking
                solved = backtracking_solver(sudoku)
            exec_time = time.time() - start_time

            if solved:
                print(f"Solution found in {exec_time:.4f} seconds")
            else:
                print("No solution found")

        pygame.display.flip()

if __name__ == "__main__":
    main()
    pygame.quit()
