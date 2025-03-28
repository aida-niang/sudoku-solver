import pygame

# Définir les couleurs
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)  # Couleur verte
BLUE = (0, 0, 255)  # Couleur bleue
RED = (255, 0, 0)  # Couleur rouge

# Dimensions de la grille
CELL_SIZE = 60
GRID_SIZE = 9

# Initialiser Pygame et la fenêtre
pygame.init()
screen = pygame.display.set_mode((CELL_SIZE * GRID_SIZE, CELL_SIZE * GRID_SIZE + 100))  # Ajouter un peu d'espace pour les boutons
pygame.display.set_caption("Sudoku Solver")

# Police
FONT = pygame.font.Font(None, 36)
