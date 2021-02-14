"""
Cours : La Programmation Orientée Objet en Python - 9/11 - L'héritage en Python [4/5]
Lien : https://www.youtube.com/watch?v=RT-Uu1yWRcc&list=PLlxQJeQRaKDSB3VOLR8s0vEMHfvUzgqfW&index=9

TDN POO leçon 9 : héritages et exceptions

Éditeur : Laurent REYNAUD
Date : 13-09-2020
"""

import utilities  # import du module 'utilities' créé qui comprend la fonction 'pluriel()'


class StatsFormatError(Exception):
    pass


class SportTeam:
    """La variable 'fine_amount' (montant de l'amende) est une variable de classe qui représente une amende
    forfaitaire de 50 000 € qui s'applique quelque soit l'équipe """
    """ Par convention pour les chiffres (entiers/réels) dépassant la centaine, on utilise le caractère '_' """
    fine_amount = 50_000

    def __init__(self, name, wins, losses):  # constructeur
        """ Les variables ci-après sont des variables d'instance car chaque équipe (chaque objet) a son propre nom,
        ses propres victoires et ses propres défaites : ces variables sont uniques à chaque équipe """
        self.name = name
        self.wins = wins
        self.losses = losses
        self.total_fines = 0  # Chaque équipe à une amende totale de 0 €

    def get_fined(self):  # méthode d'instance pour appliquer l'amende infligée à l'équipe
        self.total_fines += self.fine_amount
        """ Contrairement à Java, on ne peut pas déclarer directement la variable de classe 'fine_amount' dans une    
        méthode, il faut recourir préalablement à l'instruction 'self'. Dans ce cas là, si en dehors de la classe on    
        instruit la fonction suivante :    
        team_1.fine_amount = 25_000    
        alors le résultat affichera 25_000 qui sera applicable uniquement pour l'objet 'team_1' et cela constituera une    
        variable d'instance propre à l'objet 'team_1'.   

        Si à la place de 'self' on aurait mis le nom de la classe (l'instruction serait donc 'SportTeam.fine_amount' au   
        lieu de 'self.fine_amount'), dans ce cas là, si on instruit la fonction suivante en dehors de la classe :   
        team_1.fine_amount = 30_000    
        alors le résultat affichera la valeur de la variable de classe soit 50_000 -> l'instruction ci-dessus n'aurait   
        rien changé de la valeur de l'attribut 'fine_amount' pour l'objet 'team_1'. """

    def stats(self):  # méthode d'instance permettant d'afficher les statitiques de l'équipe
        return f"{self.name} has {utilities.pluriel(self.wins, 'win')} and " \
               f"{utilities.pluriel(self.losses, 'loss', 'losses')}"

    @classmethod  # méthode de classe
    def set_fine_amount(cls, amount):  # cette méthode a pour 1er paramètre la classe désignée par convention 'cls'
        # ainsi qu'en 2ème paramètre la variable déclarée dans cette méthode (variable d'instance) : cette méthode
        # va permettre de changer la valeur de la variable de classe 'fine_amount'
        cls.fine_amount = amount  # déclaration de la variable de classe 'fine_amount' en recourant préalablement à
        # l'instruction 'cls' dont sa valeur sera modifiée avec la variable d'instance 'amount'

    @classmethod  # méthode de classe
    def from_string(cls, stats_as_string):  # cette méthode converti des données déclarées sous la forme de str
        try:
            name, wins, losses = stats_as_string.split('-')  # conversion de la str en liste avec pour séparateur le '-'
            return cls(name, int(wins), int(losses))
        except ValueError:
            raise StatsFormatError('Format invalide !') from None

    """ La méthode from_file() a été modifiée ici en recourant à la méthode from_string() qui est similaire à cette   
    méthode, exceptée qu'il faut également supprimer les 'retour-chariot' dans le fichier.txt. En liant ces deux   
    méthodes, il n'est donc pas nécessaire de redéfinir cette méthode dans la classe dérivée 'FootballTeam' """

    @classmethod  # méthode de classe
    def from_file(cls, stats_as_file):  # cette méthode converti des données déclarées dans un fichier
        try:
            with open(stats_as_file) as file:  # suppression d'une ligne de la méthode en recourant à la méthode
                # from_string
                return cls.from_string(file.readline().strip())
        except FileNotFoundError:
            print(f"Attention le fichier '{stats_as_file}' n'existe pas !")
            raise


class BasketballTeam(SportTeam):  # la classe 'BasketballTeam' hérite de la classe 'SportTeam'

    """ Seule la méthode stats() issue de la super-classe 'SportTeam' est modifiée dans la classe 'BasketballTeam() car
    il doit-être mentionné l'intitulé de [BASKETBALL] STATS """

    def stats(self):  # méthode d'instance permettant d'afficher les statitiques de l'équipe
        return '[BASKETBALL] STATS -> ' + super().stats()
        """ L'instruction super() permet de récupérer les instructions de la méthode 'stats()' de la super-classe   
        'SportTeam' """


class FootballTeam(SportTeam):  # la classe 'FootballTeam' hérite de la classe 'SportTeam'

    """ Constructeur de la super-classe 'SportTeam' redéfinie """

    def __init__(self, name, wins, losses, draws):
        super().__init__(name, wins, losses)  # rappel de la méthode init() de la classe parente
        self.draws = draws

    """ Méthode de classe de la super-classe 'SportTeam' redéfinie en rajoutant les matchs nuls 'draws' """

    @classmethod
    def from_string(cls, stats_as_string):  # cette méthode converti des données déclarées sous la forme de str
        name, wins, losses, draws = stats_as_string.split('-')  # conversion de la str en liste avec pour séparateur
        # le '-'
        return cls(name, int(wins), int(losses), int(draws))

    """ La méthode stats() issue de la super-classe 'SportTeam' est redéfinie car il doit-être mentionné l'intitulé de   
    [FOOTBALL] STATS, ainsi que les matchs nuls obtenus pour chaque équipe de football """

    def stats(self):  # méthode d'instance permettant d'afficher les statitiques de l'équipe
        return f"[FOOTBALL] STATS --> {self.name} has {utilities.pluriel(self.wins, 'win')}, " \
               f"{utilities.pluriel(self.losses, 'loss', 'losses')} and {utilities.pluriel(self.draws, 'tie')}"


print('-' * 25, 'BASKETBALL TEAMS', '-' * 25)

# Basketball Teams

basketball_team_1 = BasketballTeam('Golden State Warriors', 1, 39)
basketball_team_2 = BasketballTeam('Los Angeles Lakers', 40, 1)
basketball_team_3 = BasketballTeam.from_string('Toronto Raptors-36-14')  # Recours à la méthode de classe
# from_string() qui permet de convertir la str en une liste
basketball_team_4 = BasketballTeam.from_file('pieces/Milwaukee.txt')
# recours à la méthode de classe from_file() qui permet de convertir un fichier en une liste

print(basketball_team_1.stats())
print(basketball_team_2.stats())
print(basketball_team_3.stats())
print(basketball_team_4.stats())

print()
print('-' * 25, 'FOOTBALL TEAMS', '-' * 25)

# Football Teams
football_team_1 = FootballTeam('New England Patriots', 12, 4, 1)
football_team_2 = FootballTeam('Kansas City Chiefs', 12, 4, 0)
football_team_3 = FootballTeam.from_string('Baltimore Ravens-14-2-2')
football_team_4 = FootballTeam.from_file('pieces/San_francisco_49ers.txt')

print(football_team_1.stats())
print(football_team_2.stats())
print(football_team_3.stats())
print(football_team_4.stats())
