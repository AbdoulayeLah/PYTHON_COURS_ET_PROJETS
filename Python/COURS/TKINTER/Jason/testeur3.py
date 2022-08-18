import tkinter
from tkinter import messagebox

'''
showerror
showinfo
showwarning
askquestion
askokcancel
askyesno
askretrycancel
'''



def fonction():
    messagebox.showerror("ERREUR","Une erreur est survenu")




app=tkinter.Tk()




btn=tkinter.Button(app,text="Déclencher une erreur",command=fonction)
btn.pack()




























#check_widget=tkinter.Checkbutton(app,text="checker",offvalue=2,onvalue=5)
#radio_widget1=tkinter.Radiobutton(app,text="Homme",value=1)
#radio_widget2=tkinter.Radiobutton(app,text="Femme",value=0)
#radio_widget1.pack()
#radio_widget2.pack()
#check_widget.pack()

#scale_widget=tkinter.Scale(app,from_=10,to=100)
#scale_widget.pack()

#spinbox_widget=tkinter.Spinbox(app,from_=1,to=10)
#spinbox_widget.pack()

#lb=tkinter.Listbox(app)
#lb.insert(1,"Windows")
#lb.insert(2,"GNU/Linux")
#lb.insert(3,"MacOS")
#lb.pack()











app.mainloop()