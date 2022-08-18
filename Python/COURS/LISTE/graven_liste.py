
notes = [ 8, 12, 10, 9, 13, 20,17,8]
print(notes)
 
#---------------------------------------- calculer la moyenne de la liste -------------------------------------

from statistics import mean
moyenne = mean(notes)
print(moyenne)

#----------------------------------------------- mélanger notre liste -----------------------------------------

from random import shuffle
shuffle(notes)
print(notes)

#-------------------------------------------------- chaine/liste -----------------------------------------------

texte=input("Entrer une chaine de la forme (email-pseudo-password) : ").split("-")
print(texte)

ma_chaine="".join(texte)
print(ma_chaine)

'''
--------------------------------------------- TP : Générateur de phrases ------------------------------------------------

#Générateur de phrases
#demander une chaine de la forme "mot1/mot2/mot3/mot4/..."
#transformer cette chaine en une liste
#la mélanger
#si le nombre d'éléments est inférieur à 10 :
    aficher seulement les 2 premiers mots
#si le nombre d'éléments est supérieur ou égale à 10 :
    aficher seulement les 3 dernier mots

'''

from random import shuffle

texte=input("Veuillez saisir un ensemble de mots sous la forme 'mot1/mot2/mot3/mot4/...' : ").split("/")

shuffle(texte)

if len(texte) < 10 :
    print(f"les 2 premiers éléments sont : {texte[:2]}")
elif len(texte) >= 10 :
    print(f"les 3 derniers éléments sont : {texte[-3:]}")