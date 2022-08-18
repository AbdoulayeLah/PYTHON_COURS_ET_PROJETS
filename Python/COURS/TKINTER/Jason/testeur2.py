import tkinter

app=tkinter.Tk()

def hello():
    mes=tkinter.Label(app,text="Hello!")
    mes.pack()


#label_welcome =tkinter.Label(app,text="Bienvenue à tous !")
#message_welcome =tkinter.Message(app,text="Bienvenue à tous et bienvenue sur la chaine")
#entry_name=tkinter.Entry(app,show="*")

button_quit=tkinter.Button(app,text="OK",command=hello)
button_quit.pack()


app.mainloop()