a = [1,2,3,4,5,6,7,8,9,10]

#------------------------------------------------------affiche la liste a de trois manières différentes-----------------

print(a[::])

print(a[:])

print(a)

#-----------------------------------------------------affiche le terme 5 de deux manières différentes--------------------

print(a[4])

print(a[-6])

#--------------------------------------------------------affiche les 7 premiers termes de la liste----------------------

print(a[:7])

#------------------------------------------------------supprime les 6 derniers termes de la liste-------------------------

print(a[:-6])

#--------------------------------------------------afficher les éléments de l'indice "2" à l'indice 4(-1)---------------

print(a[2:4])

#----------------------------------------------------------------------inverse la liste a-------------------------------

print(a[::-1])

#-------------------------------------------------------------affiche la liste par saut de 3----------------------------

print(a[::3])

#------------------------------------------------------inverse la liste et affiche par saut de 2------------------------

print(a[::-2])

'''
#----------------------------------------------affiche les 9 derniers termes de la liste de deux manières différentes---

print(a[-9:])

print(a[-9::])

#-------------------------------------------supprime les 4 premiers termes de la liste de deux manières différentes-----

print(a[4:])

print(a[4::])

'''

#----------------------------------------------------------calculer la moyenne de la liste------------------------------

from statistics import mean
moyenne = mean(a)
print(moyenne)

#-----------------------------------------------------------------mélanger la liste------------------------------------

from random import shuffle
shuffle(a)
print(a)