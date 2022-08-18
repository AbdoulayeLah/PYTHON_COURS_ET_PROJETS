import copy
'''
1. Dans une meme liste, on peut avoir des éléments de types différents
2. on peut multiplier une liste : [3]*10 nous donnes une liste de 10 termes de "3"
'''

a=["bonjour","bijou",1,"paquebot",True,234]
d=[21,13,4,12,44,21,5,21,54,1,54,76]

#--------------------------------------------------------- liste de 0 à 19 ------------------------------------------------

new_list=list(range(19))
print(new_list)

#--------------------------------------------------------- suppression / début ---------------------------------------------------------

print(a[4:])

#------------------------------------------------------------ affiche / fin --------------------------------------------------------------

print(a[-2:])

#--------------------------------------------------------- multiplier la liste -----------------------------------------------------------

print(a*3)

#------------------------------------------------------------ modifier la liste -----------------------------------------------------------

a[1]="bouclier"
print(a)

#---------------------------------------------------- modifier un sous ensemble de la liste -----------------------------------------------

a[2:4]=["thor",False]
print(a)

#------------------------------------------------------ remplacer la liste par une chaine -------------------------------------------------

a[:]="junior"
print(a)

#------------------------------------------- modifier les derniers termes ---------------------------------------------

a[-3:]=["sofia"]*3
print(a[::])

'''
------------------ DATA ---------------------

extend() : concaténer des listes
insert() : insérer un élément à une position définis 
count() : méthode le la classe list() permettant de compter le nombre d'occurence  d'un terme
remove() : permet de delete n'importe quel terme de la liste avec sa nommenclature
reverse() : méthode permettant d'inverser une liste
index() : méthode permettant de récupérer l'index d'un terme
sort() : trie la liste
enumerate : -fonction- qui donne et l'index, et son terme

'''

#----- DATA ---------- DATA ----------- DATA ---------- DATA ----------- DATA ---------- DATA ---------- DATA -------------
#--------------------------------------------------------- trie ------------------------------------------------------

d.sort()
print(d)

#--------------------------------------------------------- inverser ---------------------------------------------------------

d.reverse()
print(d)

#--------------------------------------------------------- insertion ---------------------------------------------------------

d.insert(1,132423)
print(d)

#--------------------------------------------------------- compter -----------------------------------------------------

d.count(21)
print(d)

#--------------------------------------------------- suppréssion ---------------------------------------------------

d.remove(13)
print(d)

d.pop(1)
print(d[::])

del d[1]
print(d[::])

#--------------------------------------------------------- copie de liste -----------------------------------------------------

import copy
data2=copy.deepcopy(d)
print(d)

#--------------------------------------------- concaténation de liste ----------------------------------------------

d.extend(data2) 

d+=data2

print(d)

#---------------------------------------------enumérate fonction -----------------------------------------------------

for k,v in enumerate(d):
    print(k," : ",v)

#-----------------------------------------------------------------------------------------------------------------------

'''
------------- METHODE DE CHAINE --------------

join() : transformer une liste en chaine de caractère
split() : transforme une chaine en liste , inverse de join

------------------ OTHERS ----------------------

[ import + deepcopy()] = copie de liste
'''