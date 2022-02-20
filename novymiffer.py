from tkinter import *
from PIL import ImageTk, Image
#from klassa import Objednavky
okno = Tk()
okno.title("Miffer Caffe")
okno.iconbitmap("D:/programovanie/PAJTON/tkinter ulohy/Miffer Caffe/mifferikona.ico")
okno.configure(bg = "#ebebeb")
okno.state('zoomed')

hlavna_plocha = True
def vstup(event):
    event.widget.config(bg="#d1cfcf")  
def vystup(event):
    event.widget.config(bg="#bcbcbc")    
def stol():
    return
def menu():
    global hlavna_plocha
    if hlavna_plocha:
        for k in range(len(stoly)):
            stoly[k].place_forget()
            hlavna_plocha = False
    else:
        for k in range(len(stoly)):
            stoly[k].place(relx = .7, rely = .3 + float(k/10))
            hlavna_plocha = True
obrazok_menu = ImageTk.PhotoImage(Image.open("D:/programovanie/PAJTON/tkinter ulohy/Miffer Caffe/Miffer_button.png"))
tlacidlo_menu = Button(okno, image = obrazok_menu, command = menu, borderwidth = 0).place(relx = 0, rely = 0)

ciara = Canvas(okno, width = 5000 , height = 5 , bg = "black", borderwidth = 0)
ciara.pack(pady = 250)
stoly = []
for k in range(6):
    stoly.append(Button(okno, text = "STOL " + str(k+1) , command = stol, padx = 150, pady = 30, bg = "#bcbcbc", bd = 1, relief= RIDGE))

for k in range(len(stoly)):
    stoly[k].place(relx = .7, rely = .3 + float(k/10))

for k in range(len(stoly)):
    stoly[k].bind("<Enter>", lambda k : vstup(k))
    stoly[k].bind("<Leave>", lambda k : vystup(k))
okno.mainloop()