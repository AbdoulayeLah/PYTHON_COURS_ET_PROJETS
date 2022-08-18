import tkinter
'''
#observateur
def fonction(*args):
    var_label.set(var_entry.get())

#Création et paramétrage de la fenetre
app=tkinter.Tk()
app.geometry("400x300")
app.title("Variables tkinter")


#entry
var_entry=tkinter.StringVar()
var_entry.trace("w",fonction)
entry=tkinter.Entry(app,textvariable=var_entry)

#label
var_label=tkinter.StringVar()
label=tkinter.Label(app,textvariable=var_label)

entry.pack()
label.pack()
#Boucle principale
app.mainloop()


'''

def update_observer(*args):
    
    if var_gender.get():
        var_gender_label.set("C'est un Homme")
    else :
        var_gender_label.set("C'est une Femme")
    


app=tkinter.Tk()
app.geometry("400x300")


var_gender=tkinter.IntVar()
var_gender.trace("w",update_observer)
radio1=tkinter.Radiobutton(app,text="Homme",value=1,variable=var_gender)
radio2=tkinter.Radiobutton(app,text="Femme",value=0,variable=var_gender)


var_gender_label=tkinter.StringVar()
label=tkinter.Label(app,textvariable=var_gender_label)



radio1.pack()
radio2.pack()
label.pack()
app.mainloop()