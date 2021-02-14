"""
Cours : La Programmation Orientée Objet en Python - 2/11 - Classe, Objet, Attributs et Méthodes
Lien : https://www.youtube.com/watch?v=LOp0OI-sHP8&list=PLlxQJeQRaKDSB3VOLR8s0vEMHfvUzgqfW&index=2

POO - TDN leçon 2 (aspects théoriques)

Une classe contient un ou plusieurs attributs et une ou plusieurs méthodes.
C'est grâce à une classe que l'on peut créer des objets : on peut assimiler une classe à une 'maquette' et on pourra se
baser sur cette 'maquette' afin de créer autant d'objets que l'on souhaite, comme par exemple la construction de
maisons. Les objets sont la concrétisation d'une 'maquette' et donc d'une classe.

Pour rappel, avant de se lancer à proprement parler dans la POO, il faut tout d'abord suivre les étapes suivantes :
-> Analyse : définir les grands objets
-> Le design :
    - Définir les intéractions entre chaque objet
    - Réaliser un diagramme de séquence : matérialisation sur un schéma des interactions entre chaque objet
-> La programmation :
    - Élaboration d'un diagramme de classe (similaire à l'application Argo Uml)
    - Coder sur UPYLAB

Les instructions ci-après sont inchangées par rapport à la leçon 1.

Éditeur : Laurent REYNAUD
Date : 04-09-2020
"""


def pluriel(total, singular, plural=None):
    assert isinstance(total, int) and total >= 0
    """La fonction assert varifie les conditions : ci-avant, la condition est True si le nombre saisie est un entier,    
    à défaut un message d'erreur s'affiche """
    """ La fonction isinstance () permet de voir que la variable total est un entier (2ème paramètre de la fonction)"""

    if plural is None:  # si le pluriel du mot saisi ne figure pas...
        plural = singular + "s"  # ... alors le pluriel du mot saisi se termine par 's'

    string = singular if total <= 1 else plural  # La variable string regroupe les deux paramètres de la fonction
    # pluriel() : 'singular' et 'plural=None'

    return f"{total} {string}"  # mise en forme du résultat grâce à l'instruction 'f-strings' : ce qui est en '{}'
    # concerne les paramètres de la fonction


def get_basketball_team_stats(team_name, wins, losses):
    return f"[BASKEBALL] STATS -> {team_name}: {pluriel(wins, 'victoire')} - {pluriel(losses, 'défaite')}"


def get_football_team_stats(team_name, wins, losses):
    return f"[FOOTBALL] STATS -> {team_name}: {pluriel(wins, 'victoire')} - {pluriel(losses, 'défaite')}"


if __name__ == '__main__':  # le programme est lancé à partir de cette instruction

    # Équipes de basketball

    """ Édition des données à partir des fonctions prédéfinies """
    print(get_basketball_team_stats("Golden State Warriors", 12, 39))
    print(get_basketball_team_stats("Los Angeles Lakers", 37, 11))

    """ Dans les instructions ci-après, les données sont issues d'une str convertie en liste """
    raptors_stats = "Toronto Raptors-36-14"
    data = raptors_stats.split('-')  # conversion de la str en liste avec pour séparateur le '-'
    print(get_basketball_team_stats(data[0], int(data[1]), int(data[2])))
    """    
    data[0] -> indice 0 de la liste 'data' : 'Toronto Raptors'   
    date[1] -> indice 1 de la liste 'data' : "36" qui est en str qu'il faut convertir en int   
    data[2] -> indice 2 de la liste 'data' : "14" qui est en str qu'il faut convertir en int   
    """

    """ Dans les instructions ci-après, les données sont issues d'un fichier.txt convertie en une liste """
    """ Pour rappel : l'instruction 'with open() as' ferme automatiquement le fichier, il n'est donc pas besoin de    
    recourir à l'instruction close() """
    with open('pieces/Milwaukee.txt') as file:
        # ouverture du fichier
        data = file.readline().strip().split('-')  # lecture de la première ligne avec la fonction readline() avec
        # suppression du retour de la ligne avec la fonction strip() et séparateur avec la fonction split() -> la
        # variable 'data' est une liste donc l'instruction ci-après est identique que pour la conversion de la
        # variable str 'raptors_stats' en une liste
    print(get_basketball_team_stats(data[0], int(data[1]), int(data[2])))

    # Équipes de football

    """ Édition des données à partir des fonctions prédéfinies """
    print(get_football_team_stats("New England Patriots", 12, 4))
    print(get_football_team_stats("Kansas City Chiefs", 12, 4))

    """ Dans les instructions ci-après, les données sont issues d'une str convertie en liste """
    ravens_stats = "Baltimore Ravens-14-2"
    data = ravens_stats.split('-')  # conversion de la str en liste avec pour séparateur le '-'
    print(get_football_team_stats(data[0], int(data[1]), int(data[2])))
    """    
    data[0] -> indice 0 de la liste 'data' : 'Baltimore Ravens'   
    date[1] -> indice 1 de la liste 'data' : "14" qui est en str qu'il faut convertir en int   
    data[2] -> indice 2 de la liste 'data' : "2" qui est en str qu'il faut convertir en int   
    """

    """ Dans les instructions ci-après, les données sont issues d'un fichier.txt convertie en une liste """
    with open('pieces/San_francisco_49ers.txt') as file:
        # ouverture du fichier
        data = file.readline().strip().split('-')  # lecture de la première ligne avec la fonction readline() avec
        # suppression du retour de la ligne avec la fonction strip() et séparateur avec la fonction split() -> la
        # variable 'data' est une liste donc l'instruction ci-après est identique que pour la conversion de la
        # variable str 'raptors_stats' en une liste
    print(get_basketball_team_stats(data[0], int(data[1]), int(data[2])))
