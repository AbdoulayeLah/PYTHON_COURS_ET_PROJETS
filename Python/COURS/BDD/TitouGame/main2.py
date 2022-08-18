from data.icibase import maclasse

#importer la classe maclasse
var=maclasse("database.db")


def programme():
    print("MENU PRINCIPALE\n1. Connexion\n2. Inscription")
    choix=int(input())