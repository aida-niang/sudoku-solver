def backtracking_solver(sudoku):
    def is_valid(grid, row, col, num):
        # Vérifie si le nombre peut être placé à cette position
        # Vérifier la ligne
        for i in range(9):
            if grid[row][i] == num:
                return False
        # Vérifier la colonne
        for i in range(9):
            if grid[i][col] == num:
                return False
        # Vérifier la sous-grille 3x3
        box_row, box_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(3):
            for j in range(3):
                if grid[box_row + i][box_col + j] == num:
                    return False
        return True

    def solve(grid):
        # Chercher une case vide
        for row in range(9):
            for col in range(9):
                if grid[row][col] == 0:  # Si la case est vide
                    # Essayer les chiffres de 1 à 9
                    for num in range(1, 10):
                        if is_valid(grid, row, col, num):
                            # Placer le numéro si valide
                            grid[row][col] = num
                            print(f"Essai de {num} à ({row}, {col})")  # Affichage pour suivre l'essai
                            # Appel récursif pour la prochaine case
                            if solve(grid):
                                return True
                            # Si ça ne marche pas, revenir en arrière
                            grid[row][col] = 0
                            print(f"Retour en arrière à ({row}, {col})")  # Affichage du retour
                    return False  # Aucun numéro valide n'a fonctionné
        return True  # Le Sudoku est résolu

    # Démarrer la résolution
    return solve(sudoku.grid)
