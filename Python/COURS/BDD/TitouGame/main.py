from data.icibase import maclasse
from les_fonction import fonctione
var=maclasse("database.db")
x=fonctione()


def changer_le_password(username : str):
    new_password=input("Veuiller entrer le nouveau mot de passe : ")
    new_password_confirmed=input("Veuiller confirmer le mot de passe : ")
    if new_password==new_password_confirmed:
        var.change_password(username,new_password)
        print("Votre mot de passe a bien été modifier")
    else:
        print("Les mots de passe ne correspondent pas")

def list():
    #liste des utilisateurs
    users=var.affichage()
    for i in users:
        print(i["username"])

def menu_connected(username : str):
    while True:
        print("Bienvenue sur la page principale\n1. Se déconnecter\n2. Changer le mot de passe\n3. Consulter les utilisateurs existant")
        
        choix=int(input())
        if choix==1:
            return
        elif choix ==2:
            changer_le_password(username)
        elif choix ==3:
            list()





print("MENU PRINCIPALE\n1. Connexion\n2. Inscription")
choix=int(input())

if choix==1:
    x.connexion_fonction()
elif choix==2:
    username=input("Username : ")
    password=input("password : ")
    age=int(input("age : "))
            
    var.create_user(username,password,age)
    menu_connected(username)  

else:
    print("Erreur de saisie")

