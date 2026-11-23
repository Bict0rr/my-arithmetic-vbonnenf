# SPDX-FileCopyrightText: 2026-present vbonnenf <victor.bonnenfant@etudiant.univ-lr.fr>
#
# SPDX-License-Identifier: MIT
"""Tests unitaires pour la fonction pgcd."""

from my_arithmetic_vbonnenf import pgcd


def test_pgcd_standard() -> None:
    assert pgcd(48, 18) == 6
    assert pgcd(18, 48) == 6
    assert pgcd(101, 103) == 1


def test_pgcd_equal() -> None:
    assert pgcd(12, 12) == 12


def test_pgcd_zero() -> None:
    assert pgcd(0, 5) == 5
    assert pgcd(5, 0) == 5
    assert pgcd(0, 0) == 0


def test_pgcd_negative() -> None:
    assert pgcd(-48, 18) == 6
    assert pgcd(48, -18) == 6
    assert pgcd(-48, -18) == 6
