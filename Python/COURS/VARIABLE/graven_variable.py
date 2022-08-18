
'''
#----------------------------------------------- Rolls : variable ------------------------------------------

1. la variable doit etre écris en minuscule
2. il est interdit d'ajouter des caractères spéciaux à notre variable
3. On a pas le droit de m'etre des espaces,il faut les remplacer par des "_"
4. Ne pas mettre des valeurs numériques devant le nom de la variable

'''

#----------------------------------------------- page_principale ------------------------------------------
if __name__=='__main__':
    print("c'est notre page principale")

#-------------------------------------------- les types d'affichages ---------------------------------------------

username = "Graven"
age=19

print("1. {} de {}".format(age,username))
print(f"2. {age} de {username}")
print("3.",age,"de",username)
print("4. " + str(age) + " de " + username )
