from module.grid import taille_grille



def reponse(grille):
    while True:
        try:
            ligne = int(input(f"Entrez le numéro de la ligne (1-{taille_grille}): ")) - 1
            colonne = int(input(f"Entrez le numéro de la colonne (1-{taille_grille}): ")) - 1

            if ligne in range(taille_grille) and colonne in range(taille_grille) and grille[ligne, colonne] == '':
                return ligne, colonne
            else:
                print("Case déjà occupée ou hors de la grille.")
        except ValueError:
            print("Entrée invalide. Veuillez entrer des numéros valides.")
