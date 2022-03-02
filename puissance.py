def init_puissance_4():
    return [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
    ]


board = init_puissance_4()


def affiche_puissance_4():
    pretty = '+---' * len(board[0]) + '+'

    for line in board:
        print(pretty)
        tokens = '|'
        for token in line:
            if token == 0:
                tokens += '   |'
            elif token == 1:
                tokens += ' O |'
            elif token == 2:
                tokens += ' X |'
        print(tokens)

    print(pretty)


def joue_pion(joueur: int, colonne: int):
    for i in range(5, -1, -1):
        if board[i][colonne] == 0:
            board[i][colonne] = joueur
            break


def horizontal(joueur: int):
    for line in board:
        for i in range(4):
            if line[i] == joueur and line[i] == line[i+1] and line[i] == line[i+2] and line[i] == line[i+3]:
                return True
    return False


def vertical(joueur: int):
    for i in range(6):
        for j in range(3):
            if board[j][i] == joueur and board[j][i] == board[j+1][i] and board[j][i] == board[j+2][i] and board[j][i] == board[j+3][i]:
                return True
    return False


def diagonal_gauche(joueur: int):
    for i in range(3, 6):
        for j in range(4):
            if board[i][j] == joueur and board[i][j] == board[i-1][j+1] and board[i][j] == board[i-2][j+2] and board[i][j] == board[i-3][j+3]:
                return True
    return False


def diagonal_droite(joueur: int):
    for i in range(3):
        for j in range(4):
            if board[i][j] == joueur and board[i][j] == board[i+1][j+1] and board[i][j] == board[i+2][j+2] and board[i][j] == board[i+3][j+3]:
                return True
    return False


def victoire(joueur: int):
    return horizontal(joueur) or vertical(joueur) or diagonal_gauche(joueur) or diagonal_droite(joueur)


def demarre_jeu():
    p = True
    while True:
        player = 1 if p else 2

        col = int(input(f"Joueur {player}, entrez une colonne: "))

        if col < 0 or col > 6:
            print("Colonne invalide")
            continue

        joue_pion(player, col)
        affiche_puissance_4()

        if victoire(1):
            print("Joueur 1 gagne")
            break

        if victoire(2):
            print("Joueur 2 gagne")
            break

        p = not p


demarre_jeu()
