"""
Cours : La Programmation Orientée Objet en Python - 4/11 - Variables de classe
Lien : https://www.youtube.com/watch?v=GwAoA6nvJTM&list=PLlxQJeQRaKDSB3VOLR8s0vEMHfvUzgqfW&index=4

TDN POO leçon 4 : les variables de classe
Les variables de classe sont partagées par tous les objets de la classe alors que les variables d'instance sont uniques
à chaque objet.
Une variable de classe est assimilée à une constante dans Java (excepté que le nom de la variable de classe n'est pas en
majuscules).
À la différence d'une variable de classe, une variable d'instance aura une valeur différente selon l'objet (l'équipe
ici)

Éditeur : Laurent REYNAUD
Date : 04-09-2020
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

    def get_fined(self):  # méthode pour appliquer l'amende infligée à l'équipe de Basketball
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

    def stats(self):  # méthode permettant d'afficher les statitiques de l'équipe de basketball
        return f'[BASKETBALL] STATS -> {self.name} : {self.wins} victoires - {self.losses} défaites'


team_1 = BasketballTeam('Golden State Warriors', 12, 39)
team_2 = BasketballTeam('Los Angeles Lakers', 40, 10)

print(team_1.stats())
print(team_2.stats())
team_1.fine_amount = 25_000  # Modification de l'amende forfaitaire pour l'équipe 1 qui devient donc une variable
# d'instance uniquement pour l'objet 'team_1'
team_1.get_fined()  # Et une amende infligée à l'équipe 1 !
print(team_1.total_fines)  # Résultat : 25000
team_2.get_fined()  # Et une amende infligée à l'équipe 2 soit 50 000 !
team_2.get_fined()  # Et une autre amende infligée à l'équipe 2 soit 50 000 !
print(team_2.total_fines)  # Résultat : 100000
print(BasketballTeam.number_of_teams)  # Résultat : 2 -> nombre d'équipes déclaré
