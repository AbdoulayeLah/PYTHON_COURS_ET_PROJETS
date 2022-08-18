import tkinter
from tkinter.messagebox import YES


#création et paramétrage de la fenetre
app=tkinter.Tk()
app.geometry("640x480")
app.title("Positionnement widgets")



#widgets...
"""
label=tkinter.Label(app,text="Un label")
entry=tkinter.Entry(app)
btn=tkinter.Button(app,text="BIENVENUE")

label.grid()
entry.grid()
btn.grid()
"""

btn=tkinter.Button(app,text="BIENVENUE")
btn.place(x=20,y=20)

#boucle principale
app.mainloop()