from tkinter import *
from PIL import ImageTk, Image

root = Tk()

log_ram = Canvas(root, width = 370, height = 220, bg = "#e6ffff", borderwidth = 2, relief = GROOVE).place(x = 420, y = 230)
menu_picture = ImageTk.PhotoImage(Image.open("D:/programovanie/PAJTON/tkinter ulohy/Miffer Caffe/OBRAZOK.png"))
menu_button = Label(root, image =menu_picture, bg = "white", borderwidth = 0)
menu_button.place(relx = .046, rely = .053)
root.mainloop()