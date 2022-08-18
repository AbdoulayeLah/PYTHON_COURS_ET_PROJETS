import tkinter 
#from tkinter import *

mainapp = tkinter.Tk()






















mainapp.title("Mon premier programme fenetre")
#mainapp.minsize(640,480)
#mainapp.maxsize(1280,720)
#mainapp.resizable(False,False)
#mainapp.positionfrom("user")
#mainapp.sizefrom("user")












fenetre_x=200
fenetre_y=200
ecran_x=int(mainapp.winfo_screenwidth())
ecran_y=int(mainapp.winfo_screenheight())


posx= (ecran_x//2)-(fenetre_x//2)
posy= (ecran_y//2)-(fenetre_y//2)


geo="{}x{}+{}+{}".format(fenetre_x,fenetre_y,posx,posy)

mainapp.geometry(geo)




























mainapp.mainloop()
