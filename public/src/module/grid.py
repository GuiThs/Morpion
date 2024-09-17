import numpy as np
import matplotlib.pyplot as plt

taille_grille = 3
grille = np.array([['', '', ''], ['', '', ''], ['', '', '']])
def afficher_grille(grille):
    plt.plot([1, 1], [0, 3], color='black', lw=2)
    plt.plot([2, 2], [0, 3], color='black', lw=2)
    plt.plot([0, 3], [1, 1], color='black', lw=2)
    plt.plot([0, 3], [2, 2], color='black', lw=2)

    for i in range(taille_grille):
        for j in range(taille_grille):
            if grille[i,j] == 'X':
                plt.text(j + 0.5,2.5 - i, "X", fontsize=20, ha = 'center', va = 'center', color='red')
            elif grille[i,j] == "O":
                plt.text(j + 0.5,2.5 - i,"O", fontsize = 20,ha = 'center', va = 'center', color='blue')
    plt.xlim(0,3)
    plt.ylim(0,3)
    plt.show()

def reponse(grille):
    while True: 
        try:

            ligne = int(input("Entrez le numéro de la ligne 1, 2 ou 3: ")) - 1 
            colonne = int(input("Entrez le numéro de la colonne 1, 2 ou 3: ")) - 1 

            if ligne in range(taille_grille) and colonne in range(taille_grille) and grille[ligne, colonne] == '':
                return ligne, colonne 
            else:
                print("Case déjà occupé.")
        except ValueError: 
            print("Entrée invalide.")


def placer_marque(grille, ligne, colonne, joueur):
    grille[ligne, colonne] = joueur


def match_nul(grille):
    return np.all(grille != '')


# def victoire(grille, joueur_actuel):
#     for i in range(taille_grille):
#         if np.all(grille)



def jeu():
    joueur_actuel = 'X'
    while True:
        ligne, colonne = reponse(grille)
        placer_marque(grille, ligne, colonne, joueur_actuel)
        afficher_grille(grille)
        joueur_actuel = 'O' if joueur_actuel == 'X' else 'X'
        
        if match_nul(grille):
            print("Match nul")
            break

jeu()


