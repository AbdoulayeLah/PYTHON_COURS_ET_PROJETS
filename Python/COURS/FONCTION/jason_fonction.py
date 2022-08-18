#---------------------------------------------------Valeur_par_défaut----------------------------------------------------

def fonction(x="par défaut"):
    print(x)

fonction("affiche quelque chose")
fonction()


#------------------------------------*args(nombre d'arguments variables)---------------------------------------------------


def fonction2(*encore):
    for i in encore:
        print(i)

fonction2("a","b",15,"d")




#------------------------------------*args(paramètre nommée/ sortie dico)-------------------------------------------------


def fonction3(**nommé):
    for i in nommé:
        print(nommé[i])

fonction3(a="1",b=32,c="AZERTY")