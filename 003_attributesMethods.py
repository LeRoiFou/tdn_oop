"""
Cours : La Programmation Orientée Objet en Python - 3/11 - Création de classe et d'objets
Lien : https://www.youtube.com/watch?v=Ebo_zQahWm4&list=PLlxQJeQRaKDSB3VOLR8s0vEMHfvUzgqfW&index=3

TDN POO leçon 3 : les attributs d'instance et les méthodes

Le constructeur paramétré sous Python est également définit comme une méthode de la classe concernée (instruction def())
mais qui se nomme '__init__' et a pour paramètre l'instruction 'self' et les autres attributs déclarés dans la classe.
L'instruction 'self' est une instruction dynamique qui est remplacée ci-dessous par les objets 'team_1' et 'team_2'.

Un constructeur paramétré est donc représenté de la manière suivante :
def __init__(self, attribut1, attribut2...)

Et un constructeur non paramétré est représenté de la manière suivante :
def __init__(self)

Car quelque soit la méthode d'une classe, il faut au minimum un argument en paramètre qui est 'self' par convention
(méthode non paramétré dans Java) qui équivaut à l'objet déclaré. 'Self' est nommé par convention sous Python qui
pourraît donc très bien être remplacé comme par exemple par 'salut'...

Éditeur : Laurent REYNAUD
Date : 04-09-2020
"""


class EquipeBasketBall:

    def __init__(self, name, wins, losses):  # constructeur
        self.name = name
        self.wins = wins
        self.losses = losses

    def stats(self):  # méthode permettant d'afficher les statitiques de l'équipe de basketball
        return f"[BASKETBALL] STATS -> {self.name} : {self.wins} victoires - {self.losses} défaites"


team_1 = EquipeBasketBall("Golden State Warriors", 12, 39)
team_2 = EquipeBasketBall("Los Angeles Lakers", 40, 10)

print(team_1.stats())
print(team_2.stats())
