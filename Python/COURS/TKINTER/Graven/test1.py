from tkinter import *
import webbrowser

def fonction():
    webbrowser.open_new("http://youtube.com/gravenilvectuto")


#creer une fenetre
window= Tk()





#personnaliser cette fenetre
window.title("My Application")
window.geometry("720x480")
window.minsize(480,360)
window.iconbitmap('C:/Users/lahte/OneDrive/Bureau/Python/Cours/Tkinter/Graven/logo.ico')
window.config(background='#33FFE9')

#creer la frame
var=Frame(window,bg='#33FFE9')


#ajouter un premier texte 
t1=Label(var,text="Bienvenue sur l'application", font=("Courrier",40),bg='#33FFE9',fg='white')
t1.pack(expand=YES)

#ajouter
var.pack(expand=YES)



#ajouter un second texte 
t2=Label(var,text="Hey salut à tous c'est Graven", font=("Courrier",25),bg='#33FFE9',fg='white')
t2.pack(expand=YES)


#ajouter un premier bouton
b1=Button(var,text="Ouvrir Youtube",font=("Courrier,25"),bg='white',fg='#33FFE9',command=fonction)
b1.pack(pady=25,fill=X)

#afficher
window.mainloop()  