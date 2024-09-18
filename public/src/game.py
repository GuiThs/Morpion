from module.grid import afficher_grille, grille, taille_grille
from module.reponse import reponse
from module.victoire_nul import victoire, match_nul



def placer_marque(grille, ligne, colonne, joueur):
    grille[ligne, colonne] = joueur

def jeu():
    joueur_actuel = 'X'
    while True:
        afficher_grille(grille)
        ligne, colonne = reponse(grille)
        placer_marque(grille, ligne, colonne, joueur_actuel)

        if victoire(grille, joueur_actuel):
            afficher_grille(grille)
            print(f"Le joueur {joueur_actuel} a gagné!")
            break
        elif match_nul(grille):
            afficher_grille(grille)
            print("Match nul!")
            break

        joueur_actuel = 'O' if joueur_actuel == 'X' else 'X'

jeu()
