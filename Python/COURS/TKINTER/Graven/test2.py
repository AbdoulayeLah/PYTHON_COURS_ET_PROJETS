import string
from random import randint,choice
from tkinter import *

def generate_password():
    min=6
    max=12
    all_chars= string.ascii_letters+string.punctuation+string.digits

    password="".join(choice(all_chars) for x in range(randint(min,max)))
    password_entry.delete(0,END)
    password_entry.insert(0,password)

#creation de la fenetre
window=Tk()


window.title("Générateur de mot de passe")
window.geometry("1080x720")
window.iconbitmap('C:/Users/lahte/OneDrive/Bureau/Python/Cours/Tkinter/Graven/logo.ico')
window.config(background='#4065A4')

#creer la frame principale
f1=Frame(window,bg='#4065A4')


#creation d'image
i1=PhotoImage(file='C:/Users/lahte/OneDrive/Bureau/Python/Cours/Tkinter/Graven/hop.png').zoom(35).subsample(32)
c1=Canvas(f1, width=520,height=520,bg='#4065A4',bd=0,highlightthickness=0)
c1.create_image(520/2,520/2,image=i1)
c1.grid(row=0,column=0,sticky=W)


#creer une sous boite
sb=Frame(f1,bg='#4065A4')
sb.grid(row=0,column=1,sticky=W)

#creer un titre
t1=Label(sb,text="Mot de passe",font=("Helvetica",20),bg='#4065A4',fg='white')
t1.pack()


#creer un champs/entrée/input
password_entry=Entry(sb,font=("Helvetica",20),bg='#4065A4',fg='white')
password_entry.pack(pady=15)

#creer un bouton
generate_password_button=Button(sb,text="Générer",font=("Helvetica",20),bg='#4065A4',fg='white',command=generate_password)
generate_password_button.pack(pady=15,fill=X)





#afficher la frame
f1.pack(expand=YES)



#creer une barre de menu
menu_bar=Menu(window)
#creer un premier menu
file_menu=Menu(menu_bar,tearoff=0)
file_menu.add_command(label="Nouveau",command=generate_password)
file_menu.add_command(label="Quitter",command=window.quit)
menu_bar.add_cascade(label="le menu",menu=file_menu)

#configurer notre fenetre pour ajouter cette menu bar
window.config(menu=menu_bar)

#afficher la fenetre
window.mainloop()