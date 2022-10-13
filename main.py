"""
Elouan Cassoudebat--Arcila, 407

"""
from dataclasses import dataclass
from random import randint
@dataclass
class Colors:
    """ ANSI color codes """
    BLACK = "\033[0;30m"
    RED = "\033[0;31m"
    GREEN = "\033[0;32m"
    BROWN = "\033[0;33m"
    BLUE = "\033[0;34m"
    PURPLE = "\033[0;35m"
    CYAN = "\033[0;36m"
    LIGHT_GRAY = "\033[0;37m"
    DARK_GRAY = "\033[1;30m"
    LIGHT_RED = "\033[1;31m"
    LIGHT_GREEN = "\033[1;32m"
    YELLOW = "\033[1;33m"
    LIGHT_BLUE = "\033[1;34m"
    LIGHT_PURPLE = "\033[1;35m"
    LIGHT_CYAN = "\033[1;36m"
    LIGHT_WHITE = "\033[1;37m"
    BOLD = "\033[1m"
    FAINT = "\033[2m"
    ITALIC = "\033[3m"
    UNDERLINE = "\033[4m"
    BLINK = "\033[5m"
    NEGATIVE = "\033[7m"
    CROSSED = "\033[9m"
    END = "\033[0m"

def start():
    question = input(" voulez vous, lire les regles(r), jouer(j) ou quitter(q)\n"
                     "-->")
    if question == "r":
        print(Colors.LIGHT_BLUE,
              "Pour réussir un combat, il faut que la valeur du dé lancé soit supérieure à la force de l’adversaire. \n"
              "Dans ce cas, le niveau de vie de l’usager est augmenté de la force de l’adversaire. \n"
              "Une défaite a lieu lorsque la valeur du dé lancé par l’usager est inférieure ou égale à la force \n"
              "de l’adversaire.  Dans ce cas, le niveau de vie de l’usager est diminué de la force de l’adversaire.\n"
              "La partie se termine lorsque les points de vie de l’usager tombent sous 0.\n"
              "L’usager peut combattre ou éviter chaque adversaire, dans le cas de l’évitement, il y a une pénalité\n"
              "de 1 point de vie.")
    if question == "q":
        print(Colors.LIGHT_RED,
              "Merci et au revoir... ")
    if question == "j":
        game()

def game():
    print()

start()
