from random import randint
import fonction_jeu_devinette as function

from random import randint

#differentes fonctions du jeu
def mot_aleatoire() :
    liste_mot = ["vision", "python" , "java"]
    choix = randint(0 , len(liste_mot)-1)
    mot = liste_mot[choix]
    return mot
def affiche_mot_a_deviner(mot_mystere) :

    mot_caché = ''
    for cpt in range(len(mot_a_deviner)) :
        if cpt% 2 == 0 :
            mot_caché += mot_a_deviner[cpt]
        else :
            mot_caché += "_"
    print(f"\nVoici le mot a deviner : {mot_caché}")

    return 


def saisie_mot() :
    while True :
        try :
            mot = input("Quelle mot suggérer vous  : ") 
            
            for i in mot : 
                if i is int :
                    raise ValueError("vous avez entré un nombre au lieu d'un mot.")

        except :
            print("vous avez entrer un nombre ou un mot mélangé de chiffre. ")
        else : 
            break
    return mot

# programme du jeu 
mot_a_deviner = mot_aleatoire()
nbr_tentative = 2 

print("******************Jeu de devinette de mot********************")

affiche_mot_a_deviner(mot_a_deviner)

while nbr_tentative > 0 :

    mot_util = saisie_mot()

    if mot_util == mot_a_deviner :
        print(f"Bravo vous avez trouver le mot mystere.\nLe mot chercher est bien : {mot_a_deviner}")
        break
    else : 
        print("vous avez entrer une réponse incorrecte")
        nbr_tentative -= 1
    if nbr_tentative == 0 :
        print("vous avez perdu..\nMerci d'avoir jouer.")

