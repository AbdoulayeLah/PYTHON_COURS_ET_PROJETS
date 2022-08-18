from data.icibase import maclasse
from main import menu_connected
var=maclasse("database.db")


class fonctione():

    def __init__(self):
        pass




    def connexion_fonction(self):
        username=input("Username : ")
        password=input("password : ")
        if var.user_exists(username) and password == var.verification_connexion(username) :
            menu_connected(username)
        else:
            print("Nom d’utilisateur ou mot de passe incorrect")