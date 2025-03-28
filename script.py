import pygame

class SudokuGrid:
    def __init__(self, grid):
        self.grid = grid

    @staticmethod
    def from_file(filename):
        with open(filename, "r") as f:
            grid = []
            for line in f.readlines():
                # Remplacer les underscores par 0 pour les cases vides
                line = line.strip().replace('_', '0')  # Remplacer '_' par '0'
                grid.append(list(map(int, line.split())))
        
        # Vérification de la grille après chargement
        if len(grid) != 9 or any(len(row) != 9 for row in grid):
            raise ValueError("La grille doit être de taille 9x9.")
        
        print("Grille chargée :")
        for row in grid:
            print(row)

        return SudokuGrid(grid)

    def is_valid(self, row, col, num):
        # Vérifie si le nombre peut être placé à cette position
        for i in range(9):
            if self.grid[row][i] == num or self.grid[i][col] == num:
                return False
        # Vérifier la sous-grille 3x3
        box_row, box_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(3):
            for j in range(3):
                if self.grid[box_row + i][box_col + j] == num:
                    return False
        return True

    def brute_force_solver(self):
        # Vérification de la grille (9x9)
        if len(self.grid) != 9 or any(len(row) != 9 for row in self.grid):
            raise ValueError("La grille du Sudoku doit être de taille 9x9")
        
        # Démarrer la résolution
        def solve(grid):
            for row in range(9):
                for col in range(9):
                    if grid[row][col] == 0:  # Cherche une case vide
                        for num in range(1, 10):  # Essayer les chiffres de 1 à 9
                            grid[row][col] = num
                            if self.is_valid(row, col, num):
                                if solve(grid):
                                    return True
                            grid[row][col] = 0  # Réinitialiser la case si nécessaire
                        return False  # Si aucun chiffre valide n'est trouvé
            return True  # Si toutes les cases sont remplies

        solve(self.grid)

    def display(self):
        for row in self.grid:
            print(row)

    def pygame_display(self):
        # Initialiser Pygame
        pygame.init()

        # Définir les dimensions de l'écran
        screen = pygame.display.set_mode((450, 450))
        pygame.display.set_caption("Sudoku Solver")

        # Couleurs
        WHITE = (255, 255, 255)
        BLACK = (0, 0, 0)
        GREY = (200, 200, 200)

        # Dimensions des cases
        cell_size = 50
        font = pygame.font.Font(None, 40)

        # Boucle principale pour l'affichage
        running = True
        while running:
            screen.fill(WHITE)

            # Afficher la grille
            for row in range(9):
                for col in range(9):
                    x = col * cell_size
                    y = row * cell_size
                    pygame.draw.rect(screen, BLACK, (x, y, cell_size, cell_size), 2)

                    # Remplir les cases avec les numéros
                    if self.grid[row][col] != 0:
                        text = font.render(str(self.grid[row][col]), True, BLACK)
                        screen.blit(text, (x + 15, y + 10))

            # Afficher les lignes de la grille
            for i in range(1, 9):
                if i % 3 == 0:
                    pygame.draw.line(screen, BLACK, (i * cell_size, 0), (i * cell_size, 450), 4)
                    pygame.draw.line(screen, BLACK, (0, i * cell_size), (450, i * cell_size), 4)
                else:
                    pygame.draw.line(screen, GREY, (i * cell_size, 0), (i * cell_size, 450), 1)
                    pygame.draw.line(screen, GREY, (0, i * cell_size), (450, i * cell_size), 1)

            # Mettre à jour l'affichage
            pygame.display.flip()

            # Gérer les événements Pygame
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

        pygame.quit()

def main():
    # Charger un fichier Sudoku
    try:
        sudoku = SudokuGrid.from_file("examples/sudoku.txt")

        # Afficher la grille avant la résolution
        print("Grille avant résolution :")
        sudoku.display()

        # Résolution par Force Brute
        print("\nRésolution avec Force Brute :")
        sudoku.brute_force_solver()

        # Afficher la solution
        print("\nGrille résolue :")
        sudoku.display()

        # Affichage de la solution avec Pygame
        sudoku.pygame_display_
