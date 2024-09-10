# ce fichier renferme toutes les fonctions qui seront utilisées dans le jeu

from random import randint 
def Nombre_aleatoire() :   # cette fonction permet de génerer un nombre aléatoire en fonction du niveau choisi par le joueur

    print("**********************Jeu de nombre mystere**********************\n")
    print("Voici les différentes options : ")
    print("\t1.Facile\n\t2.Moyen\n\t3.DIfficile\n")

    choix = saisie_joueur(1)      # récupération du niveau saisi par le joueur

    if choix == 1 :
        nbr_aleatoire = randint(0 , 50)
    elif choix == 2 :
        nbr_aleatoire = randint(0 , 150)
    elif choix == 3 :
        nbr_aleatoire = randint(0 , 200)

    return nbr_aleatoire


def aide_joueur(nbr_mystere, proposition) : # cette fonction aide le joueur à trouver le nombre mystere
    difference = nbr_mystere - proposition
    difference = abs(difference)
    if difference < 5 :
        print("\nvous etes très pret du nombre mystere.\n ")
    elif difference < 15 :
        print("\nvous etes un peu pret du nombre.\n")
    elif difference > 15 : 
        print("\nvous etes loin du nombre mystere.\n")


def saisie_joueur(a) :     # permet de récupérer les saisies de l'utilisateur de manière sécurisée

    if a == 1 :
        nbr_aleatoire = 0
        choix = 0 
        while(True):     # controle de la sasie de l'utilisateur.on vérifie si la saisie n'est pas differente des chiffres 1 , 2 , 3
            try :
                choix = int(input("Quel niveau choisissez-vous : "))
                if(nbr_aleatoire < 0 or choix > 3 ) :
                    raise ValueError("vous avez entrer un nombre négatif ou superieur à la valeur maximal autorisée.")
            except :
                print("\nVous avez entrez un caractère différent d'un chiffre ou soit vous avez entrer un nombre négatif ou superieur à la valeur maximal autorisée.")
                print("Veuillez ressaisir votre choix.")
            else :
                break 
        return choix 

    elif a == 2 :
        nombre = 0 
        while True : 
            try :
                nombre = int(input("Quel nombre proposez-vous :  "))
                if nombre < 0 :
                    raise ValueError("le nombre entré ne dois pas etre négative")
            except :
                print("vous avez entré des caractères invalides.")
            else : break
        return nombre 
    
