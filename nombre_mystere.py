import fonction_nombre_mystere as function
from time import  sleep 


nbr_tentative = 16
nbr_mystere = function.Nombre_aleatoire()        # récupération du nombre aléatoire
print("Début du jeu...")
sleep(1)
while nbr_tentative > 0 :

    proposition = function.saisie_joueur(2)
    if proposition == nbr_mystere :
        print(f"Bravo!!! \nVous avez trouvez le mot mystere en {16-nbr_tentative} tentative(s).")
        break
    else :
        function.aide_joueur(nbr_mystere, proposition )
        nbr_tentative -= 1

    if nbr_tentative == 0 :
        print("vous avez perdu.")



