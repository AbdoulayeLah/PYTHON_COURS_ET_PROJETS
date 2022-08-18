#--------------------------------------les variables locales et globales--------------------------------------------------

def change_x():
    global x
    x+=1
    
x=20

change_x()
print(x)
change_x()
print(x)


#------------------------------------------------utiliser return-----------------------------------------------------------


def addition():
    return 5+5

def message():
    return "renvoie aussi du texte : "
print(message(),addition())

#------------------------------------------------entrer des paramètres----------------------------------------------------



    #variable locale:si on entre en paramètre une information quelconque, lui ajouter 5 puis le retourner
    # la valeur par défaut du paramètre est 0
def addition(x=0):
    return 5+x

n=12
print(addition(32))


#----------------------fonction max() qui va renvoyer le résultat le plus haut parmis 2 valeur----------------------------

def max(x,y):
    if x>y:
        return x
    elif x<y:
        return y

first_value=int(input("Entrer la première valeur : "))
second_value=int(input("Entrer la seconde valeur : "))
print("lavaleur max est : ",max(first_value,second_value))


#-------------------------------------------------------la récursivité-----------------------------------------------------
                                       #une fonction peut s'appeler elle meme et former une boucle#

def add(x):
    x+=1
    print(x)
    if x<10:
        add(x)

add(0)


#------------------------------petit exo sur la récursivité pour former une boucle----------------------------------------

n=0

def exo(x):
    global n
    x+=1
    print(x)
    n+=1
    if n<=10:
        exo(x)
        

exo(3)


#----------------------------------------------------------TP------------------------------------------------------------
#tp : une fonction pour calculer le nombre de voyelles dans un mot #

'''
1. Définir une fontion get_vowels_numbers(mot)
2. Créer un compteur de voyelles 
3. Pour chaque lettre du mot, vous vérifier s'il s'agit d'une voyelle
4. Si c'est le cas, on ajoute 1 au compteur
5. A la fin de la fonction, vous aller renvoyer le compteur
'''


mot=input("mot : ")
consonnes=["b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","z"]

def voyelles(le_mot):
    mot_list=list(le_mot)
    size=len(mot_list)
    compteur=0
    index=0
    while index<size:
        if mot_list[index] not in consonnes:
            compteur+=1
        index+=1

    print("Le mot contient ",compteur," consonnes")


voyelles(mot)

