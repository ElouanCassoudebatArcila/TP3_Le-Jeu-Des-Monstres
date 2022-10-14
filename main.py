"""
Elouan Cassoudebat--Arcila, 407

"""
from time import sleep
from random import randint
from color import Colors

force_adversaire = 0
vie_joueur = 20


def start():
    print(Colors.UNDERLINE + Colors.BOLD + Colors.LIGHT_WHITE +
         "\n"
         "Combat De Monstres:\n")
    sleep(0.5)
    print(Colors.BLUE +
    "lire les regles (r)\n")
    sleep(0.5)
    print(Colors.GREEN +
    "    jouer (j)\n")
    sleep(0.5)
    print(Colors.RED +
    "   quitter (q)\n")
    sleep(0.5)
    question = input(Colors.LIGHT_WHITE +
                    "------->")
    if question == "r":
        print(Colors.LIGHT_BLUE,
              "Pour réussir un combat, il faut que la valeur du dé lancé soit supérieure à la force de l’adversaire. \n"
              "Dans ce cas, le niveau de vie de l’usager est augmenté de la force de l’adversaire. \n"
              "Une défaite a lieu lorsque la valeur du dé lancé par l’usager est inférieure ou égale à la force \n"
              "de l’adversaire.  Dans ce cas, le niveau de vie de l’usager est diminué de la force de l’adversaire.\n"
              "La partie se termine lorsque les points de vie de l’usager tombent sous 0.\n"
              "L’usager peut combattre ou éviter chaque adversaire, dans le cas de l’évitement, il y a une pénalité\n"
              "de 1 point de vie.\n"
              "")
        start()
    if question == "q":
        print(Colors.LIGHT_RED,
              "Merci et au revoir... ")
    if question == "j":
        game()

def door():
    force_adversaire = randint(1, 5)
    print(Colors.LIGHT_RED +
         "Vous tombez face à face avec un adversaire de difficulté :",force_adversaire, )

def game():
    vie_joueur = 20

    print(Colors.GREEN +
         "Vous avez 20 points de vie")
    door()



start()
