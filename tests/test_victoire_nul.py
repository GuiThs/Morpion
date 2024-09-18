import os
import sys
import numpy as np
sys.path.insert(0,
                os.path.abspath(
                    os.path.join(
                        os.path.dirname(__file__),
                        ".."
                    )
                ))

from module.grid import taille_grille
from module.victoire_nul import match_nul

def test_match_nul():
    grille = np.array([['X', 'X', 'O'], ['X', 'O', 'O'], ['O', 'X', 'X']])
    assert match_nul(grille)

