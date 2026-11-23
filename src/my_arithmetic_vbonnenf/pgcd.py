# SPDX-FileCopyrightText: 2026-present vbonnenf <victor.bonnenfant@etudiant.univ-lr.fr>
#
# SPDX-License-Identifier: MIT
"""Module de calcul arithmétique."""


def pgcd(a: int, b: int) -> int:
    """Calcule le plus grand commun diviseur (PGCD) de deux entiers.

    Utilise l'algorithme d'Euclide.

    Parameters
    ----------
    a : int
        Premier entier.
    b : int
        Second entier.

    Returns
    -------
    int
        Le plus grand commun diviseur positif (ou nul si a == 0 et b == 0)
        de ``a`` et ``b``.

    Examples
    --------
    >>> pgcd(48, 18)
    6
    >>> pgcd(0, 5)
    5
    """
    a, b = abs(a), abs(b)
    while b != 0:
        a, b = b, a % b
    return a
