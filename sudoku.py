import settings
import pygame

class Sudoku:
    def __init__(self, grid):
        self.grid = grid

    def is_valid(self, row, col, num):
        for i in range(9):
            if self.grid[row][i] == num or self.grid[i][col] == num:
                return False

        box_row, box_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(3):
            for j in range(3):
                if self.grid[box_row + i][box_col + j] == num:
                    return False
        return True

    def find_empty_cell(self):
        for row in range(9):
            for col in range(9):
                if self.grid[row][col] == 0:
                    return row, col
        return None

    def draw_grid(self, screen):
        for row in range(9):
            for col in range(9):
                x = col * settings.CELL_SIZE
                y = row * settings.CELL_SIZE
                pygame.draw.rect(screen, settings.BLACK, (x, y, settings.CELL_SIZE, settings.CELL_SIZE), 2)
                if self.grid[row][col] != 0:
                    text = settings.FONT.render(str(self.grid[row][col]), True, settings.BLACK)
                    screen.blit(text, (x + settings.CELL_SIZE // 3, y + settings.CELL_SIZE // 3))

    def highlight_cell(self, row, col, screen):
        x = col * settings.CELL_SIZE
        y = row * settings.CELL_SIZE
        pygame.draw.rect(screen, settings.RED, (x, y, settings.CELL_SIZE, settings.CELL_SIZE), 5)

    def draw_buttons(self, screen):
        # Dessiner les boutons
        button_rect_1 = pygame.Rect(settings.WIDTH // 4 - settings.BUTTON_WIDTH // 2, settings.HEIGHT - 80, settings.BUTTON_WIDTH, settings.BUTTON_HEIGHT)
        button_rect_2 = pygame.Rect(3 * settings.WIDTH // 4 - settings.BUTTON_WIDTH // 2, settings.HEIGHT - 80, settings.BUTTON_WIDTH, settings.BUTTON_HEIGHT)

        # Bouton 1 : Résolution avec Backtracking
        pygame.draw.rect(screen, settings.BUTTON_COLOR, button_rect_1)
        text_1 = settings.FONT.render("Solve (Backtracking)", True, settings.TEXT_COLOR)
        screen.blit(text_1, (button_rect_1.x + (settings.BUTTON_WIDTH - text_1.get_width()) // 2, button_rect_1.y + (settings.BUTTON_HEIGHT - text_1.get_height()) // 2))

        # Bouton 2 : Résolution avec Brute Force
        pygame.draw.rect(screen, settings.BUTTON_COLOR, button_rect_2)
        text_2 = settings.FONT.render("Solve (Brute Force)", True, settings.TEXT_COLOR)
        screen.blit(text_2, (button_rect_2.x + (settings.BUTTON_WIDTH - text_2.get_width()) // 2, button_rect_2.y + (settings.BUTTON_HEIGHT - text_2.get_height()) // 2))

        return button_rect_1, button_rect_2

    def check_button_click(self, pos):
        # Vérifier si un bouton est cliqué
        button_rect_1, button_rect_2 = self.draw_buttons(pygame.display.get_surface())
        if button_rect_1.collidepoint(pos):
            return 'backtracking'
        elif button_rect_2.collidepoint(pos):
            return 'brute_force'
        return None
