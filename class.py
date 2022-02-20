class Plocha:
    def __init__(self, master):
        self.ram = Frame(master, width = 3000 , height = 1200 , bg = "white", borderwidth = 0).pack(pady = 40, padx = 60)
        self.ram_objednavky = Frame(self.ram, width = 450 , height = 250 , bg = "#e6ffff", borderwidth = 2, relief = GROOVE)
        self.ram_objednavky.place(relx = .12 , rely = .4)
        self.obrazok_menu = ImageTk.PhotoImage(Image.open("D:/programovanie/PAJTON/tkinter ulohy/Miffer Caffe/Miffer_button.png"))
        self.tlacidlo_menu = Button(self.ram, image = self.obrazok_menu, command = self.menu, bg = "white", borderwidth = 0)
        self.tlacidlo_menu.place(relx = .046, rely = .053)
        self.ciara = Canvas(self.ram, width = 650 , height = 5 , bg = "black", borderwidth = 0).place(relx = .12, rely = .32)
        self.stoly = []
        self.objednavky = ["Prvy stol", "Druhy stol","Treti stol", "Stvrty stol","Piaty stol", "Siesty stol"]
        global k
        for k in range(6):
            self.stoly.append(Button(self.ram, text = "STÔL " + str(k+1) , command = lambda k=k: self.stol(k), padx = 120, pady = 22, bg = "#006080", fg = "white", bd = 1, relief= FLAT, font = ("Helvetica", "10") ))
            self.stoly[k].place(relx = .7, rely = .23 + float(k/9))
            self.stoly[k].bind("<Enter>", lambda k : vstup(k))
            self.stoly[k].bind("<Leave>", lambda k : vystup(k))
        self.tlacidlo_menu.bind("<Enter>", self.vstup_main)
        self.tlacidlo_menu.bind("<Leave>", self.vystup_main)
        self.info_objednavky = Label(self.ram, text = "Stoly čakajúce na svoje objednávky : ", font = ("Helvetica", "12"), bg = "white")
        self.info_objednavky.place(relx = .12 , rely = .35)
    def menu(self):
        global hlavna_plocha
        if hlavna_plocha:
            self.info_objednavky.place_forget()
            self.ram_objednavky.place_forget()
            hlavna_plocha = False
        else:
            self.info_objednavky.place(relx = .12 , rely = .35)
            self.ram_objednavky.place(relx = .12 , rely = .4)
            hlavna_plocha = True
    def stol (self, args):
        self.nove_okno = Toplevel()
        self.nove_okno.geometry('500x350')
        self.nove_okno.geometry("+{}+{}".format(450, 200))
        self.nove_okno.title(f"Stol cislo {args + 1}")
        self.nove_okno.iconbitmap("D:/programovanie/PAJTON/tkinter ulohy/Miffer Caffe/mifferikona.ico")
        self.label_objednavka = Label (self.nove_okno, text = self.objednavky[args]).pack()
    def vstup_main(self, event):
        self.tlacidlo_menu.configure(bg = "#3a7ca5")
    def vystup_main(self, event):
        self.tlacidlo_menu.configure(bg = "white")