import json

eleves={'camille':8,'paul':12,'theo':17}

#1. afficher la valeur d'une clé

print(eleves['paul'])

#2. Gérer les exceptions

print(eleves.get('lea','None'))

#3. ajouter l'éleve léa à la dico eleves

eleves['lea'] = 20

#4. afficher les différentes clés du dictionnaire

for i in eleves:
    print(i)

#5. modifier la clé camille par zidane

      #1 methode
eleves['zidane']=eleves['camille']
del eleves['camille']

      #1 methode
eleves['zidane']=eleves.pop('camille')

#6. supprimer la clé paul

del eleves['paul']

#7. afficher uniquement les différentes valeurs du dictionnaires

for i in eleves.values():
    print(i)

#8. calculer la moyennes de la classe

print(round(sum(eleves.values())/len(eleves)))

#9. boucle qui va afficher le prénom et la moyenne de chaque élève de deux manières

      #1 methode
for i in eleves.items():
    print(i)

      #2 methode
for prenom,note in eleves.items():
    print(f"{prenom} : {note}")

#10. faire une copie de eleves
eleves2=eleves.copy()
print(eleves2)

#----------------------DICO DE DICO-----------------------

les_eleves={
    'camille':{'note':8,'appréciation':'insuffisant'},
    'paul':{'note':12,'appréciation':'encouragement'},
    'theo':{'note':18,'appréciation':'félicitation'}
    }

#11. récupérer l'appréciation de théo

print(les_eleves['theo']['appréciation'])

#12. ajouter l'élève léa au dico les_eleves

les_eleves['lea']={'note':15,'appréciation':'très bien'}

#13. modifier la note d'un eleve sur les_eleves

les_eleves['camille']['note']=20

#14. verifier qu'une eleve existe dans la classe

if 'camille' in les_eleves.keys():
    print("L'élève fait partis de la classe")
else:
    print("L'élève ne fait pas partis de la classe")

#15. supprimer une eleve

del les_eleves['theo']

#16. récupérer les notes et les appréciations de chaque élève de deux manières différentes

      #1 methode
for i in les_eleves:
    print(f" {i} : {les_eleves[i]['note']} : {les_eleves[i]['appréciation']}")

      #2 methode
for i in les_eleves.keys():
    print(f" {i} : {les_eleves[i]['note']} : {les_eleves[i]['appréciation']}")


#17. sauvegarder notre classe dans un fichier json (javascript object notation)

with open('save.json','w+') as file:
    json.dump(eleves,file)
    
#18. charger les données depuis le fichier 

with open('save.json','r') as file:
    le_nouveau_eleves=json.load(file)

#19. modifier l'appréciation de paul sur les_eleves

les_eleves['paul']['appréciation']='très moyen'

#20. modifier le nom de paul par edouard et sa moyenne par 19 

     #1 méthode
les_eleves['edouard']=les_eleves['paul']
del les_eleves['paul']

     #2 méthode
les_eleves['edouard']=les_eleves.pop('camille')