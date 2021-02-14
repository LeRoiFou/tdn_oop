"""
Cours : La Programmation Orientée Objet en Python - 5/11 - Méthodes de classe et Méthodes statiques
Lien : https://www.youtube.com/watch?v=aNvfPOFGYx0&list=PLlxQJeQRaKDSB3VOLR8s0vEMHfvUzgqfW&index=5

TDN POO leçon 5 (suite) : méthode utilisée dans plusieurs classes

Au lieu de déclarer une méthode statique dans une classe, si on sait que cette méthode va être utiliser dans plusieurs
classes, alors dans ce cas on déclare cette méthode statique comme une fonction dans un module
Cette fois-ci, comme pour les modules de Python, à chaque fois qu'on apppelle la fonction 'pluriel' on doit saisir
préalablement le module auquel il est rattaché, soit : 'utilities.pluriel()'

Éditeur : Laurent REYNAUD
Date : 05-09-2020
"""


def pluriel(total, singular, plural=None):
    # Cette fonction permet de mettre aux pluriels les mots de 'victoire' t de 'défaite'

    assert isinstance(total, int) and total >= 0

    if plural is None:
        plural = singular + 's'

    string = singular if total <= 1 else plural

    return f'{total} {string}'
