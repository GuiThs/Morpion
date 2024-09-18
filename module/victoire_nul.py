import numpy as np
from module.grid import taille_grille



def match_nul(grille):
    return np.all(grille != '')

def victoire(grille, joueur_actuel):
    for i in range(taille_grille):
        if np.all(grille[i, :] == joueur_actuel) or np.all(grille[:, i] == joueur_actuel):
            return True
    if np.all(np.diag(grille) == joueur_actuel) or np.all(np.diag(np.fliplr(grille)) == joueur_actuel):
        return True
    return False
