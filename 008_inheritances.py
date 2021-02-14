"""
Cours : La Programmation Orientée Objet en Python - 6/11 - L'héritage en Python [1/5]
Lien : https://www.youtube.com/watch?v=WnvoC09Q_Vs&list=PLlxQJeQRaKDSB3VOLR8s0vEMHfvUzgqfW&index=6

TDN POO leçon 6 : héritages
Les classes d'équipe de basketball et de football héritent de la super-classe 'SportTeam' qui permet d'éviter de faire
des erreurs en dupliquant les données d'une équipe à une autre équipe.

Pour mettre en héritage une classe, l'instruction suivante est à réaliser :
class NomClasse(Super-classe)
Les sous-classes héritent des attributs et des méthodes de la super-classe, mais il est également possible de modifier
les attributs et les méthodes de la super-classe rattachée en intervant directement dans la sous-classe concernée : on
dit dans ce cas que les attributs / les méthodes modifiés sont redéfinis.
À défaut de redéfinir les méthodes / les attributs de la classe parente, il suffit juste de saisir l'instruction 'pass'
dans la sous-classe concernée.

À la différence de Java, en Python une classe peut hériter de plusieurs super-classes.

Éditeur : Laurent REYNAUD
Date : 05-09-2020
"""

import utilities  # import du module 'utilities' créé qui comprend la fonction 'pluriel()'


class SportTeam:
    fine_amount = 50_000
    number_of_teams = 0
    """ Les variable 'fine_amount' (montant de l'amende) et 'number_of_teams' (nombre d'équipe) sont des variables de  
    classe : 
    -> La variable 'fine_amount' est une amende forfaitaire de 50 000 € qui s'applique quelque soit l'équipe 
    -> La variable 'number_of_teams' est le nombre d'équipe """
    """ Par convention pour les chiffres (entiers/réels) dépassant la centaine, on utilise le caractère '_' """

    def __init__(self, name, wins, losses):  # constructeur
        """ Les variables ci-après sont des variables d'instance car chaque équipe (chaque objet) a son propre nom,
        ses propres victoires et ses propres défaites : ces variables sont uniques à chaque équipe """
        self.name = name
        self.wins = wins
        self.losses = losses
        self.total_fines = 0  # Chaque équipe à une amende totale de 0 €
        SportTeam.number_of_teams += 1  # À chaque équipe déclarée on rajoute 1

    def get_fined(self):  # méthode d'instance pour appliquer l'amende infligée à l'équipe
        self.total_fines += self.fine_amount
        """ Contrairement à Java, on ne peut pas déclarer directement la variable de classe 'fine_amount' dans une  
        méthode, il faut recourir préalablement à l'instruction 'self'. Dans ce cas là, si en dehors de la classe on  
        instruit la fonction suivante :  
        team_1.fine_amount = 25_000  
        alors le résultat affichera 25_000 qui sera applicable uniquement pour l'objet 'team_1' et cela constituera une  
        variable d'instance propre à l'objet 'team_1'. 

        Si à la place de 'self' on aurait mis le nom de la classe (l'instruction serait donc  
        'SportTeam.fine_amount' au lieu de 'self.fine_amount'), dans ce cas là, si on instruit la fonction  
        suivante en dehors de la classe :  
        team_1.fine_amount = 30_000  
        alors le résultat affichera la valeur de la variable de classe soit 50_000 -> l'instruction ci-dessus n'aurait 
        rien changé de la valeur de l'attribut 'fine_amount' pour l'objet 'team_1'. 

        Cependant, on peut voir que la variable de classe 'number_of_teams' est initialisée dans le constructeur de la 
        classe, avec préalablement le nom de la classe ('SportTeam.number_of_teams += 1'). 
        Or, si on aurait initialisé cet attribut avec l'instruction 'self', le compteur du nombre d'équipe ne 
        fonctionnerait que pour chaque équipe (la variable ne serait applicable que pour chaque objet) et au final le 
        compteur tomberait à 0 (voir également ce programme sur Python tutor)."""

    def stats(self):  # méthode d'instance permettant d'afficher les statitiques de l'équipe
        return f"{self.name} a {utilities.pluriel(self.wins, 'victoire')} et " \
               f"{utilities.pluriel(self.losses, 'défaite')}"

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


class BasketballTeam(SportTeam):  # la classe 'BasketballTeam' hérite de la classe 'SportTeam'

    """ Seule la méthode stats() issue de la super-classe 'SportTeam' est modifiée dans la classe 'BasketballTeam() car
    il doit-être mentionné l'intitulé de [BASKETBALL] STATS """

    def stats(self):  # méthode d'instance permettant d'afficher les statitiques de l'équipe
        return '[BASKETBALL] STATS ->' + super().stats()
        """ L'instruction super() permet de récupérer les instructions de la méthode 'stats()' de la SUPER-classe 
        'SportTeam' """


class FootballTeam(SportTeam):  # la classe 'FootballTeam' hérite de la classe 'SportTeam'

    """ Seule la méthode stats() issue de la super-classe 'SportTeam' est modifiée dans la classe 'FootballTeam() car
    il doit-être mentionné l'intitulé de [FOOTBALL] STATS """

    def stats(self):  # méthode d'instance permettant d'afficher les statitiques de l'équipe
        return '[FOOTBALL] STATS -->' + super().stats()
        """ L'instruction super() permet de récupérer les instructions de la méthode 'stats()' de la SUPER-classe 
        'SportTeam' """


class SoccerTeam(SportTeam):  # la classe 'SoccerTeam' hérite de la classe 'SportTeam'

    """ Seule la méthode stats() issue de la super-classe 'SportTeam' est modifiée dans la classe 'SoccerTeam() car
    il doit-être mentionné l'intitulé de [soccer] STATS """

    def stats(self):  # méthode d'instance permettant d'afficher les statitiques de l'équipe
        return '[SOCCER] STATS -->' + super().stats()
        """ L'instruction super() permet de récupérer les instructions de la méthode 'stats()' de la SUPER-classe 
        'SportTeam' """


print('-' * 25, 'BASKETBALL TEAMS', '-' * 25)

# Basketball Teams

basketball_team_1 = BasketballTeam('Golden State Warriors', 1, 39)
basketball_team_2 = BasketballTeam('Los Angeles Lakers', 40, 1)
basketball_team_3 = BasketballTeam.from_string('Toronto Raptors-36-14')  # Recours à la méthode de classe
# from_string() qui permet de convertir la str en une liste
basketball_team_4 = BasketballTeam.from_file('Pieces/Milwaukee.txt')
# recours à la méthode de classe from_file() qui permet de convertir un fichier en une liste

print(basketball_team_1.stats())
print(basketball_team_2.stats())
print(basketball_team_3.stats())
print(basketball_team_4.stats())
basketball_team_1.fine_amount = 25_000  # Modification de l'amende forfaitaire pour l'équipe 1 qui devient donc
# une variable d'instance uniquement pour l'objet 'BasketballTeam_team_1'
basketball_team_1.get_fined()  # Et une amende infligée à l'équipe 1 !
print(basketball_team_1.total_fines)  # Résultat : 25000
basketball_team_2.get_fined()  # Et une amende infligée à l'équipe 2 soit 50 000 !
basketball_team_2.get_fined()  # Et une autre amende infligée à l'équipe 2 soit 50 000 !
print(basketball_team_2.total_fines)  # Résultat : 100000
print(BasketballTeam.number_of_teams)  # Résultat : 2 -> nombre d'équipes déclaré
BasketballTeam.set_fine_amount(75_000)  # Recours à la méthode de classe en modifiant le montant forfaitaire de l'amende
basketball_team_2.get_fined()  # Et une autre amende infligée à l'équipe 2 soit 75 000 !
print(basketball_team_2.total_fines)  # Résultat : 175000
basketball_team_1.get_fined()  # L'objet team_1 dispose déjà d'une variable d'instance concerne l'amende pour un
# montant de 25000
print(basketball_team_1.total_fines)  # Résultat : 50000

print()
print('-' * 25, 'FOOTBALL TEAMS', '-' * 25)

# Football Teams
football_team_1 = FootballTeam('New England Patriots', 12, 4)
football_team_2 = FootballTeam('Kansas City Chiefs', 12, 4)
football_team_3 = FootballTeam.from_string('Baltimore Ravens-14-2')
football_team_4 = FootballTeam.from_file('pieces/San_francisco_49ers.txt')
print(football_team_1.stats())
print(football_team_2.stats())
print(football_team_3.stats())
print(football_team_4.stats())

print()
print('-' * 25, 'SOCCER TEAMS', '-' * 25)

# Soccer Teams
soccer_team_1 = SoccerTeam('Chelsea', 13, 8)
soccer_team_2 = SoccerTeam('Real de Madrid', 10, 3)
soccer_team_3 = SoccerTeam.from_string('Liverpool-16-1')
soccer_team_4 = SoccerTeam.from_file('Pieces/Juventus.txt')
print(soccer_team_1.stats())
print(soccer_team_2.stats())
print(soccer_team_3.stats())
print(soccer_team_4.stats())
