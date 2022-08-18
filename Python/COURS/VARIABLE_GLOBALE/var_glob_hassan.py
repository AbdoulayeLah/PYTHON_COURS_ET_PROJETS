#----> variable locale = variable définit à l'intérieur d'une fonction
#----> si on définit une variable locale, on peut pas l'utiliser de manière globale sur la page principale
#----> variable globale = variable définit en dehors de toutes les fonctions
#----> la variable globale est accéssible en lecture selement a l'intérieur de la fonction
#----> le mot réservé global permet de "modifier" une variable global dans une fonction

#---------------------------------------------------- exercice 1 ------------------------------------------------------


'''

def f(x,y):
    global a
    a=45
    x,y=y,x
    b=17
    # a=45 b=17 x=81 y=9
    print(a,b,x,y)




#variable global a=3 b=15 x=3 y=4
#a peut etre modifier a l'intérieur de la fonction
a,b,x,y=3,15,3,4

f(9,81)
print(a,b,x,y)
# a=45 b=15 x=3 y=4
'''



#---------------------------------------------------- exercice 2 ------------------------------------------------------


'''

a=1

def f():
    print(a)
def g():
    a=2
    print(a)#var_loc
def h():
    global a 
    a=3
    print(a)


print(a)#1
f()#1
print(a)#1
g()#2/loc
print(a)#1
h()#a modifier : #3
print(a)#3
#111.2.1.33

'''


#---------------------------------------------------- exercice 3 ------------------------------------------------------


z=0 
def f():
    global z
    z=3

def g(x,y):
    global z
    return x+y+z

f()
total=g(4,5)
print(total)

#ZZ=0  
#ZZ=3
#total=12
#print(12)