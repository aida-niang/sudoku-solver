def brute_force_solver(sudoku):
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
                        # Tester le chiffre pour la case
                        grid[row][col] = num
                        # Si ce numéro est valide, continuer avec la prochaine case
                        if is_valid(grid, row, col, num):
                            # Appel récursif pour résoudre la grille avec cette nouvelle valeur
                            if solve(grid):
                                return True
                        # Si aucun chiffre valide n'est trouvé, réinitialiser la case et tester le suivant
                        grid[row][col] = 0
                    return False  # Aucun chiffre valide n'a fonctionné dans cette case
        return True  # Toutes les cases sont remplies, sudoku résolu

    # Démarrer la résolution en appelant solve
    return solve(sudoku.grid)
