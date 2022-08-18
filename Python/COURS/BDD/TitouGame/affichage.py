from tkinter import *
app=Tk()




#personnaliser cette fenetre
app.geometry("300x150")
app.title("LAYE_APPLICATION")
app.iconbitmap("C:/Users/lahte/OneDrive/Bureau/logo.ico")
app.config(background='gray')
app.resizable(False,False)



#créé les label du menu 1
label_1=Label(app,text="MENU PRINCIPALE",bg='gray',font=("Courrier"),fg='blue')
label_2=Label(app,text="1. Connexion",bg='gray')
label_3=Label(app,text="2. Inscription",bg='gray')

#champ de saisie du menu 1
ent1=Entry(app)

label_1.pack()
label_2.pack()
label_3.pack()
ent1.pack()












app.mainloop()