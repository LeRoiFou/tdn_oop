"""
Cours : La Programmation Orientée Objet en Python - 5/11 - Méthodes de classe et Méthodes statiques
Lien : https://www.youtube.com/watch?v=aNvfPOFGYx0&list=PLlxQJeQRaKDSB3VOLR8s0vEMHfvUzgqfW&index=5

TDN POO leçon 5 : méthodes de classes et méthodes statiques

Les méthodes d'instances reçoivent en 1er argument l'objet sur lequel on travaille et donc par convention on a recours à
l'instruction 'self' en 1er paramètre :
def nom_methode (self, parametre2, parametre3...)

Les méthodes de classes reçoivent en 1er argument la classe sur laquelle on travaille et donc par convention on a
recours à l'instruction 'cls' en 1er paramètre et en saisissant préalablement à la déclaration d'une méthode de classe
un décorateur désigné '@classmethod' :
@classmethod
def nom_methode (cls, parametre2, parametre3...)
Les méthodes de classes sont désignées sous Python comme des constructeurs additionnels

Les méthodes statiques ne reçoivent rien en 1er argument -> elles sont assimilées à des fonctions classiques qu'on a
recours en dehors de la POO, mais elles sont ajoutées dans une classe car elles ont une fonction à réaliser dans la
classe où elles sont rattachées. Avant de déclarer une méthode statique, on doit saisir préalablement un décorateur
désigné '@staticmethod' :
@staticmethod
def nom_methode (parametre1, parametre2...)

Éditeur : Laurent REYNAUD
Date : 05-09-2020
"""


class BasketballTeam:
    fine_amount = 50_000
    number_of_teams = 0
    """ Les variable 'fine_amount' (montant de l'amende) et 'number_of_teams' (nombre d'équipe) sont des variables de  
    classe : 
    -> La variable 'fine_amount' est une amende forfaitaire de 50 000 € qui s'applique quelque soit l'équipe de  
    basketball  
    -> La variable 'number_of_teams' est le nombre d'équipe de basketball """
    """ Par convention pour les chiffres (entiers/réels) dépassant la centaine, on utilise le caractère '_' """

    def __init__(self, name, wins, losses):  # constructeur
        """ Les variables ci-après sont des variables d'instance car chaque équipe de Basketball (chaque objet) a son
        propre nom, ses propres victoires et ses propres défaites : ces variables sont uniques à chaque équipe """
        self.name = name
        self.wins = wins
        self.losses = losses
        self.total_fines = 0  # Chaque équipe à une amende totale de 0 €
        BasketballTeam.number_of_teams += 1  # À chaque équipe déclarée on rajoute 1

    def get_fined(self):  # méthode d'instance pour appliquer l'amende infligée à l'équipe de Basketball
        self.total_fines += self.fine_amount
        """ Contrairement à Java, on ne peut pas déclarer directement la variable de classe 'fine_amount' dans une  
        méthode, il faut recourir préalablement à l'instruction 'self'. Dans ce cas là, si en dehors de la classe on  
        instruit la fonction suivante :  
        team_1.fine_amount = 25_000  
        alors le résultat affichera 25_000 qui sera applicable uniquement pour l'objet 'team_1' et cela constituera une  
        variable d'instance propre à l'objet 'team_1'. 

        Si à la place de 'self' on aurait mis le nom de la classe (l'instruction serait donc  
        'BasketballTeam.fine_amount' au lieu de 'self.fine_amount'), dans ce cas là, si on instruit la fonction  
        suivante en dehors de la classe :  
        team_1.fine_amount = 30_000  
        alors le résultat affichera la valeur de la variable de classe soit 50_000 -> l'instruction ci-dessus n'aurait 
        rien changé de la valeur de l'attribut 'fine_amount' pour l'objet 'team_1'. 

        Cependant, on peut voir que la variable de classe 'number_of_teams' est initialisée dans le constructeur de la 
        classe, avec préalablement le nom de la classe ('BasketballTeam.number_of_teams += 1'). 
        Or, si on aurait initialisé cet attribut avec l'instruction 'self', le compteur du nombre d'équipe de basketball 
        ne fonctionnerait que pour chaque équipe (la variable ne serait applicable que pour chaque objet) et au final le 
        compteur tomberait à 0 (voir également ce programme sur Python tutor)."""

    def stats(self):  # méthode d'instance permettant d'afficher les statitiques de l'équipe de basketball
        return f"[BASKETBALL] STATS -> {self.name} : {self.pluriel(self.wins, 'victoire')} - " \
               f"{self.pluriel(self.losses, 'défaites')}"

    @classmethod  # méthode de classe
    def set_fine_amount(cls, amount):  # cette méthode à pour 1er paramètre la classe désignée par convention
        # 'cls' ainsi qu'en 2ème paramètre la variable déclarée dans cette méthode (variable d'instance) : cette méthode
        # va permettre de changer la valeur de la variable de classe 'fine_amount'
        cls.fine_amount = amount  # déclaration de la variable de classe 'fine_amount' en recourant préalablement à
        # l'instruction 'cls' dont sa valeur sera modifiée avec la variable d'instance 'amount'

    @classmethod  # méthode de classe
    def from_string(cls, stats_as_string):  # cette méthode converti des données déclarées sous la forme de str
        name, wins, losses = stats_as_string.split('-')  # conversion de la str en liste avec pour séparateur le '-'
        return cls(name, int(wins), int(losses))

    @classmethod  # méthode de classe
    def from_file(cls, stats_as_file):  # cette méthode converti des données déclarées dans un fichier
        with open(stats_as_file) as file:
            name, wins, losses = file.readline().strip().split('-')
            return cls(name, int(wins), int(losses))

    @staticmethod  # méthode statique
    def pluriel(total, singular, plural=None):  # cette méthode permet de mettre aux pluriels les mots de 'victoire'
        # et de 'défaite'
        pass
        assert isinstance(total, int) and total >= 0

        if plural is None:
            plural = singular + 's'

        string = singular if total <= 1 else plural

        return f'{total} {string}'


team_1 = BasketballTeam('Golden State Warriors', 1, 39)
team_2 = BasketballTeam('Los Angeles Lakers', 40, 1)
team_3 = BasketballTeam.from_string('Toronto Raptors-36-14')  # Recours à la méthode de classe from_string() qui
# permet de convertir la str en une liste
team_4 = BasketballTeam.from_file('Pieces/Milwaukee.txt')  #
# recours à la méthode de classe from_file() qui permet de convertir un fichier en une liste

print(team_1.stats())
print(team_2.stats())
print(team_3.stats())
print(team_4.stats())
team_1.fine_amount = 25_000  # Modification de l'amende forfaitaire pour l'équipe 1 qui devient donc une variable
# d'instance uniquement pour l'objet 'team_1'
team_1.get_fined()  # Et une amende infligée à l'équipe 1 !
print(team_1.total_fines)  # Résultat : 25000
team_2.get_fined()  # Et une amende infligée à l'équipe 2 soit 50 000 !
team_2.get_fined()  # Et une autre amende infligée à l'équipe 2 soit 50 000 !
print(team_2.total_fines)  # Résultat : 100000
print(BasketballTeam.number_of_teams)  # Résultat : 2 -> nombre d'équipes déclaré
BasketballTeam.set_fine_amount(75_000)  # Recours à la méthode de classe en modifiant le montant forfaitaire de l'amende
team_2.get_fined()  # Et une autre amende infligée à l'équipe 2 soit 75 000 !
print(team_2.total_fines)  # Résultat : 175000
team_1.get_fined()  # L'objet team_1 dispose déjà d'une variable d'instance concerne l'amende pour un montant de 25000
print(team_1.total_fines)  # Résultat : 50000
