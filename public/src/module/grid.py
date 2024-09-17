import numpy as np
import matplotlib.pyplot as plt


def afficher_grille():
    plt.plot([1, 1], [0, 3], color='black', lw=2)
    plt.plot([2, 2], [0, 3], color='black', lw=2)
    plt.plot([0, 3], [1, 1], color='black', lw=2)
    plt.plot([0, 3], [2, 2], color='black', lw=2)
    
    plt.show()
    
    


afficher_grille()