import numpy as np
import matplotlib.pyplot as plt


taille_grille = 3
grille = np.array([['', '', ''], ['', '', ''], ['', '', '']])

plt.ion()


def afficher_grille(grille):
    plt.clf()
    plt.plot([1, 1], [0, 3], color='black', lw=2)
    plt.plot([2, 2], [0, 3], color='black', lw=2)
    plt.plot([0, 3], [1, 1], color='black', lw=2)
    plt.plot([0, 3], [2, 2], color='black', lw=2)

    for i in range(taille_grille):
        for j in range(taille_grille):
            if grille[i, j] == 'X':
                plt.text(j + 0.5, 2.5 - i, "X", fontsize=20, ha='center', va='center', color='red')
            elif grille[i, j] == "O":
                plt.text(j + 0.5, 2.5 - i, "O", fontsize=20, ha='center', va='center', color='blue')

    plt.xlim(0, 3)
    plt.ylim(0, 3)
    plt.show()
