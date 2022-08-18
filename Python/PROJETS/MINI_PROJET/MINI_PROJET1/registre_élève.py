#Création de registres qui vont stocker les élèves et leurs notes avec gestion d'erreur et enregistrement
from statistics import mean
import time





moyenne_élève=list()
registre_classe=dict()
moyenne_liste=dict()
list_sum=list()
nouvelle_liste=list()





z=0
while z==0:
    #création des registres
    matière={"maths":0,"pc":0,"hg":0,"francais":0,"anglais":0}


    def registre(var=0):
        global registre_classe
        global moyenne_liste
        #-------------------------------------------initialisation matière





        #---------------------------------------------------------nom élève
        nom_élève=input("Veuillez saisir le nom de l'élève : ")

        var=0

        #---------------------------------------------------enregistrement notes
        maths_note=int(input("maths : "))
        matière["maths"]=maths_note
        var=var+maths_note

        pc_note=int(input("pc : "))
        matière["pc"]=pc_note
        var=var+pc_note

        hg_note=int(input("hg : "))
        matière["hg"]=hg_note
        var=var+hg_note

        francais_note=int(input("francais : "))
        matière["francais"]=francais_note
        var=var+francais_note

        anglais_note=int(input("anglais : "))
        matière["anglais"]=anglais_note
        var=var+anglais_note

        moyenne_liste[nom_élève]=(var/5)
        #---------------------------------------------------------------------




        #enregistrer l'élève
        registre_classe[nom_élève]=matière



    rang=1

    def clé(val):
        global rang
        for key,value in moyenne_liste.items():
            if val==value:
                print(f"{rang} | {key} | {value}")
                rang+=1
        









    def menu():
        print("--------------------------------------------------------------------------------------------------------------------------------------------------------------")
        print("1. Enregistrer les notes d'un élève ")
        print("2. Voir le bulletin d'un élève")
        print("3. Voir la moyenne d'un élève")
        print("4. Voir la moyenne de la classe")
        print("5. Registre de la classe")
        print("6. Afficher la liste des élèves")
        print("7. Le rang des élèves")







        saisie=int(input())
        time.sleep(2)













        if saisie==1:
            #1. Enregistrer les notes d'un élève 
            registre()
            time.sleep(2)










        elif saisie==2:
            #2. Voir le bulletin d'un élève
            nom_de_élève=input("Veuillez saisir le nom de l'élève : ")
            time.sleep(2)
            print(f"Bulletin de l'élève {nom_de_élève} : ",registre_classe.get(nom_de_élève,f"{nom_de_élève} n'est pas enregistrer"))
            time.sleep(2)
            #afficher_note  










        elif saisie==3:
            #3. Voir la moyenne d'un élève
            nom_élève_moyenne=input("Veuillez saisir le nom de l'élève : ")
            time.sleep(2)
            print(f"Moyenne de l'élève {nom_élève_moyenne} : ",moyenne_liste.get(nom_élève_moyenne,f"{nom_élève_moyenne} n'est pas enregistrer"))
            time.sleep(2)
            











        elif saisie==4:
            #4. Voir la moyenne de la classe
            time.sleep(2)
            x=0
            for i in moyenne_liste.values():
                x=x+i
            moyenne=x/(len(moyenne_liste))
            print(f"Moyenne de la classe est : {moyenne}")
            
        







        elif saisie==5:
            #5. Registre de la classe
            print("Registre de la classe : ",registre_classe)
            time.sleep(2)

        





        elif saisie==6:
            #6. Afficher la liste des élèves
            print("La liste des élèves : ")
            for i in registre_classe.keys():
                print(i)
            




        elif saisie==7:
            #7. le rang des élèves

            for i in moyenne_liste.values():
                nouvelle_liste.append(i)

    
            
            for y in range(len(nouvelle_liste)):
                clé(max(nouvelle_liste))
                nouvelle_liste.remove(max(nouvelle_liste))






        else:
            print("Erreur de saisie")
            time.sleep(2)


    menu()














