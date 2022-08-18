


def somme(init = 5, *nbr, **key):
   r = init
   for n in nbr:
      r+=n
   for k in key:
      r+=key[k]
   return r


print(somme(100,2,2, x=20, y=10))


#etudier les expressions régulièresf "r"
import re
x = 'I am fine'
regex = re.compile('(?P<subject>\w+) (?P<verb>\w+) (?P<adjective>\w+)')
out = re.search(regex, x)
print(out.groupdict())


try: 
   list = 2*[0]+2*[5] 
   x = list[2] 
   print('OK!') 
except IndexError: 
   print('Block Except!') 
else: 
   print('Block Else!') 
finally: 
   print('Block Finally!')





def fun(): 
    str = "WayToLearnX"
    nbr = 1
    return str, nbr;  
str, nbr = fun()  # Affecter le tuple renvoyé
print(str) 
print(nbr)





def bonjour(nb):
    return nb + a

a=5
print(bonjour(10))
