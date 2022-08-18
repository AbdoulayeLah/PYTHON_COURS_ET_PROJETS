#----------------------------------------------------------- BREAK -------------------------------------------------------


'''
break : permet de | sortir d'une boucle for/while | sous une certaine "condition" |  et executer les instructions suivantes |


            exercice : Ecrire un programme qui calcule la somme d'un maximum de 8 nombres entrés par 
            l'utilisateur, 
            condition : si un nombre négatif est entré, la boucle est terminé et le résultat afficher

'''

somme=0
for i in range(8):
    print("Valeur ",i+1," : ",end="")
    nombre=int(input())
    if nombre>=0:
        somme=somme+nombre
    elif nombre<0:
        continue

print("La somme des nombre positif saisie est ",somme)


#--------------------------------------------------------- CONTINUE -----------------------------------------------------

