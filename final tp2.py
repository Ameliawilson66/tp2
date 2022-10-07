#Amelia Wilson 401
#tp2

import random

def jeu_devinette():
    nombre_random = random.randint(0, 1000)
    max = 100
    min = 0
    print('jai choisit un nombre entre 0 et 1000.')
    guess = input('nombre: ')
    nb_essai = 0

    while guess != nombre_random:
        nb_essai += 1

        if guess < nombre_random:
            guess = int(input("le nombre est plus grand: "))

        if guess > nombre_random:
            guess = int(input("le nombre est plus petit: "))

        while guess == nombre_random:
            print("bravo! vous avez devinez le bon nombre en " + str(nb_essai) + "essais.")
            rejouer = str(input("voulez-vous rejouer. oui ou non"))
            if rejouer == "oui":
                jeu_devinette()
            if rejouer == "non":
                exit()


jeu_devinette()