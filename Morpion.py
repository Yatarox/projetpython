import random


def creer_grille():
    # Crée un cadrillage vide
    grille = [
        ["-", "-", "-"],
        ["-", "-", "-"],
        ["-", "-", "-"],
    ]

    return grille


def condition_victoire(grille):
    # Vérifie s'il y a une victoire en ligne, colonne ou diagonale
    for i in range(3):
        if grille[i][0] == grille[i][1] == grille[i][2] != "-" or grille[0][i] == grille[1][i] == grille[2][i] != "-":
            return True
    # Vérifie la victoire en diagonale
    if grille[0][0] == grille[1][1] == grille[2][2] != "-" or grille[0][2] == grille[1][1] == grille[2][0] != "-":
        return True
    else:
        return False


def jouer_bot(grille):
    # Le bot essaie de gagner ou de bloquer l'adversaire
    choix=random.randint(1,5)
    #fait un coup aléatoire si choix tombe sur 1
    if choix==1:
        print("coup random")
        x = random.randint(0, 2)
        y = random.randint(0, 2)
        return x, y
    for i in range(3):
        if "O" == grille[i][0] == grille[i][1] != "-" and grille[i][2] == "-":
            return i, 2
        elif "O" == grille[i][0] == grille[i][2] != "-" and grille[i][1] == "-":
            return i, 1
        elif "O" == grille[i][1] == grille[i][2] != "-" and grille[i][0] == "-":
            return i, 0
        # Vérifie les colonnes
        elif "O" == grille[0][i] == grille[1][i] != "-" and grille[2][i] == "-":
            return 2, i
        elif "O" == grille[0][i] == grille[2][i] != "-" and grille[1][i] == "-":
            return 1, i
        elif "O" == grille[1][i] == grille[2][i] != "-" and grille[0][i] == "-":
            return 0, i

    # Vérifie les diagonales
    if "O" == grille[0][0] == grille[1][1] != "-" and grille[2][2] == "-":
        return 2, 2
    elif "O" == grille[0][0] == grille[2][2] != "-" and grille[1][1] == "-":
        return 1, 1
    elif "O" == grille[1][1] == grille[2][2] != "-" and grille[0][0] == "-":
        return 0, 0
    elif "O" == grille[0][2] == grille[1][1] != "-" and grille[2][0] == "-":
        return 2, 0
    elif "O" == grille[0][2] == grille[2][0] != "-" and grille[1][1] == "-":
        return 1, 1
    elif "O" == grille[1][1] == grille[2][0] != "-" and grille[0][2] == "-":
        return 0, 2

    for i in range(3):
        # Vérifie les lignes
        if grille[i][0] == grille[i][1] != "-" and grille[i][2] == "-":
            return i, 2
        elif grille[i][0] == grille[i][2] != "-" and grille[i][1] == "-":
            return i, 1
        elif grille[i][1] == grille[i][2] != "-" and grille[i][0] == "-":
            return i, 0
        # Vérifie les colonnes
        elif grille[0][i] == grille[1][i] != "-" and grille[2][i] == "-":
            return 2, i
        elif grille[0][i] == grille[2][i] != "-" and grille[1][i] == "-":
            return 1, i
        elif grille[1][i] == grille[2][i] != "-" and grille[0][i] == "-":
            return 0, i

    # Vérifie les diagonales
    if grille[0][0] == grille[1][1] != "-" and grille[2][2] == "-":
        return 2, 2
    elif grille[0][0] == grille[2][2] != "-" and grille[1][1] == "-":
        return 1, 1
    elif grille[1][1] == grille[2][2] != "-" and grille[0][0] == "-":
        return 0, 0
    elif grille[0][2] == grille[1][1] != "-" and grille[2][0] == "-":
        return 2, 0
    elif grille[0][2] == grille[2][0] != "-" and grille[1][1] == "-":
        return 1, 1
    elif grille[1][1] == grille[2][0] != "-" and grille[0][2] == "-":
        return 0, 2

    # Si aucune opportunité de gagner, place aléatoirement
    x = random.randint(0, 2)
    y = random.randint(0, 2)
    return x, y


def grille_complete(grille):
    # Vérifie si la grille est complète (pas de case libre)
    for i in range(3):
        for j in range(3):
            if grille[i][j] == "-":
                return False
    print("Il n'y a plus de place")
    return True


def jouer_morpion():
    grille_jeu = creer_grille()
    jeu_fini = False
    while not jeu_fini:
        verfication_erreur = False
        # verifie que la case n'est pas déja utliser ou qu'il sorte du morpion
        while not verfication_erreur:
            x = int(input("Ligne (1-3): "))
            y = int(input("Colonne (1-3): "))
            if x <= 3 and y <= 3:
                if grille_jeu[x - 1][y - 1] == "-":

                    print("plus de 3")
                    grille_jeu[x - 1][y - 1] = "X"
                    jeu_fini = condition_victoire(grille_jeu)
                    for ligne in grille_jeu:
                        print(" ".join(ligne))
                    verfication_erreur = True
                else:
                    print("case utilisée")
            else:
                print("erreur")

        if jeu_fini:
            print("Le jeu est fini")
            break
        jeu_fini = grille_complete(grille_jeu)

        if not jeu_fini:
            verfication_erreur = False
            while not verfication_erreur:
                x_bot, y_bot = jouer_bot(grille_jeu)
                if grille_jeu[x_bot][y_bot] == "-":
                    grille_jeu[x_bot][y_bot] = "O"
                    jeu_fini = condition_victoire(grille_jeu)
                    for ligne in grille_jeu:
                        print(" ".join(ligne))
                    verfication_erreur = True


def jeu():
    print("Le jeu vidéal trop s1pa")
    continuer_partie = False
    while not continuer_partie:
        jouer_morpion()
        reponse = input("Veux-tu continuer ? [Oui/Non] ").lower()
        if reponse == "non":
            continuer_partie = True
        elif reponse != "oui":
            print("Pas compris le programme ce fini")
            break


jeu()
