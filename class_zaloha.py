class Plocha:
    def __init__(self, master):
        #frames for the app
        self.frame = Frame(master, width = 3000 , height = 1200 , bg = "white", borderwidth = 0).pack(pady = 40, padx = 60)
        
        self.frame_orders = Frame(self.frame, width = 450 , height = 250 , bg = "#e6ffff", borderwidth = 2, relief = GROOVE)
        
        self.info_orders = Label(self.frame, text = "Nedostatok tovaru v databáze : ", font = ("Helvetica", "12"), bg = "white")
        
        

        # menu button stuff 
        self.menu_picture = ImageTk.PhotoImage(Image.open("D:/programovanie/PAJTON/tkinter ulohy/Miffer Caffe/Miffer_button.png"))
        self.menu_button = Button(self.frame, image = self.menu_picture, command = self.menu, bg = "white", borderwidth = 0)
        self.menu_button.place(relx = .046, rely = .053)
        self.menu_button.bind("<Enter>", self.main_input)
        self.menu_button.bind("<Leave>", self.main_output)


        # pointless stuff
        self.line = Canvas(self.frame, width = 650 , height = 5 , bg = "black", borderwidth = 0).place(relx = .12, rely = .32)
        self.user = Label(self.frame, text = f"User : {username.get().strip()}", bg = "white" , font = ("Helvetica", 10))
        self.user.place(x = 1150, y = 685)
        self.user.bind("<Enter>", self.show_user)
        self.user.bind("<Leave>", self.hide_user)

       


        # buttons for tables
        self.tables = []
        self.orders = ["Prvy stol", "Druhy stol","Treti stol", "Stvrty stol","Piaty stol", "Siesty stol"]
        global k
        for k in range(6):
            self.tables.append(Button(self.frame, text = "STÔL " + str(k+1) , command = lambda k=k: self.table(k), padx = 120, pady = 22, bg = "#006080", fg = "white", bd = 1, relief= FLAT, font = ("Helvetica", "10") ))
            self.tables[k].place(relx = .7, rely = .23 + float(k/9))
            self.tables[k].bind("<Enter>", lambda k : inputt(k))
            self.tables[k].bind("<Leave>", lambda k : output(k))

        self.user_info_frame = Frame(self.frame, width = 220, height = 100, bg = "#e6ffff", borderwidth = 2, relief = GROOVE)

        self.user_info_label = Label(self.user_info_frame, text = f"Užívateľské meno: {log_user} \n Online od : {time}", fg = "black", bg = "#e6ffff")
        self.user_info_label.pack(pady = 10, padx = 10)
        

        

    # menu button function, to make another widgets disappear   
    def menu(self):
        global main_window
        if main_window:
            self.frame_orders.place(relx = .12 , rely = .4)
            self.info_orders.place(relx = .12 , rely = .35)
            main_window = False
        else:
            self.info_orders.place_forget()
            self.frame_orders.place_forget()
            main_window = True


    # table function, making new window and show the order        
    def table (self, args):
        self.new_window = Toplevel()
        self.new_window.geometry('850x600')
        self.new_window.configure(bg = '#006080')
        self.new_window.resizable(False, False)
        self.new_window.geometry("+{}+{}".format(450, 200))
        self.new_window.title(f"Stol cislo {args + 1}")
        self.new_window.iconbitmap("D:/programovanie/PAJTON/tkinter ulohy/Miffer Caffe/mifferikona.ico")
        self.new_frame = Frame(self.new_window, width = 700 , height = 600 , bg = "white", borderwidth = 0)
        self.new_frame.pack(pady = 40, padx = 40)
        self.info_label_order = Label (self.new_window, text = f"Objednávky pre stôl č. {args + 1}", bg = "white").place(x = 150, y = 75)
        self.info_line = Canvas(self.new_window, width = 350 , height = 3 , bg = "black").place(x = 150, y = 95)
        self.table_order = requests.post('https://miffer.000webhostapp.com/getstol.php', json={'id_stol': args + 1})
        self.table_order_list = self.table_order.json()
        self.table_order_string = '\n'
        



        #frame for orders with scrollbar


        self.scroll_frame = Frame(self.new_frame, width = 50, height = 50)
        self.scroll_frame.place(x = 75, y = 95)

        self.scrollbar = Scrollbar(self.scroll_frame)
        self.scrollbar.pack(side='right', fill='y')

        self.listbox = ttk.Treeview(self.scroll_frame, selectmode='browse', yscrollcommand= self.scrollbar.set)
        # load the listbox

        self.listbox["columns"] = ("1", "2", "3", "4")
        self.listbox['show'] = 'headings'
        self.listbox.column("1", width=100, anchor='c')
        self.listbox.column("2", width=100, anchor='c')
        self.listbox.column("3", width=100, anchor='c')
        self.listbox.column("4", width=100, anchor='c')
        self.listbox.heading("1", text="Tovar ")
        self.listbox.heading("2", text="Cena ")
        self.listbox.heading("3", text="Poznámka ")
        self.listbox.heading("4", text="Stav ")
        self.table_order = requests.post('https://miffer.000webhostapp.com/getstol.php', json={'id_stol': args + 1})
        self.table_order_list = self.table_order.json()
        for i in range(len(self.table_order_list)):
            if self.table_order_list[i]['stav'] == "1":
                self.listbox.insert("",'end',text="L1",values=(self.table_order_list[i]['nazov'], self.table_order_list[i]['cena'] + ' €', self.order_comment(self.table_order_list[i]['poznamka']), 'Vybavené'))
            else:
                self.listbox.insert("",'end',text="L1",values=(self.table_order_list[i]['nazov'], self.table_order_list[i]['cena'] + ' €', self.order_comment(self.table_order_list[i]['poznamka']), 'Objednané'))

        self.listbox.pack()
        self.scrollbar.config(command=self.listbox.yview)
        self.table_order_price = requests.post('https://miffer.000webhostapp.com/getcena.php', json={'stol': args + 1})
        if self.table_order_price.json()[0]['cena'] != None:
             self.order_price = Label(self.new_frame, text = f"Cena spolu : {self.table_order_price.json()[0]['cena']} €" , bg = 'white', justify = LEFT).place(x = 75, y = 330)
        else:
            self.order_price = Label(self.new_frame, text = f"Cena spolu : 0 €" , bg = 'white', justify = LEFT).place(x = 75, y = 330)
        



        # payment

        pay = Button(self.new_frame, text = 'Zaplatiť', relief = FLAT, bg = "#006080", fg = "white", command = self.pay)

        if len(self.table_order_list) != 0:
            pay.place(x = 445, y = 330)

    

    # order comment function
    def order_comment(self, order_compare):
        if order_compare == "":
            return "-"
        else:
            return order_compare


    # pay button
    def pay(self):
        self.pay_frame = Frame(self.new_window, width = 275, height = 175, bg = 'white', bd = 2, relief = SOLID)
        self.pay_frame.place(x = 280, y = 225)
        self.pay_card = Button(self.pay_frame, text = 'Platba kartou', relief = FLAT, bg = "#006080", fg = "white", pady = 42, padx = 15, command = self.pay_card)
        self.pay_cash = Button(self.pay_frame, text = 'Platba \n v hotovosti', relief = FLAT, bg = "#006080", fg = "white" ,pady = 35, padx = 20, command =  self.pay_cash)
        self.exit_payment = Button(self.pay_frame, text = 'Zrušiť', relief = FLAT, bg = "#006080", fg = "white", padx = 5, command = self.drop_payment)
        self.pay_cash.place(x = 17, y = 15)
        self.pay_card.place(x = 143, y = 15)
        self.exit_payment.place(x = 110, y = 135)


      # card pay method

    def pay_card(self):
        global num
        print("ok") 
        self.completeName = os.path.join(save_path, f'blocek{num}.txt')
        self.file1 = open(self.completeName, "w")
        



        self.toFile = '''============================== 
      \tMiffer Caffe   
tovar:             \tcena:   
'''

        for i in range(len(self.table_order_list)):
            if len(self.table_order_list[i]['nazov']) < 5:
                self.toFile += self.table_order_list[i]['nazov'] + '\t\t\t\t' + self.table_order_list[i]['cena'] + ' €\n'
            elif len(self.table_order_list[i]['nazov']) < 8:
                self.toFile += self.table_order_list[i]['nazov'] + '\t\t\t' + self.table_order_list[i]['cena'] + ' €\n'
            else:
                self.toFile += self.table_order_list[i]['nazov'] + '\t\t' + self.table_order_list[i]['cena'] + ' €\n'
        

        self.toFile += f'''------------------------------
platba :           \t{self.table_order_price.json()[0]['cena']} €
platba kartou - akceptovaná
==============================
      
'''
        self.file1.write(self.toFile)

        self.file1.close()
        num += 1 




    # exit button function for payment 

    def drop_payment(self):
        self.pay_frame.place_forget()


  

    # cash pay method 

    def pay_cash(self):
        global num
        self.completeName = os.path.join(save_path, f'blocek{num}.txt')
        self.file1 = open(self.completeName, "w")
        



        self.toFile = '''============================== 
      \tMiffer Caffe   
tovar:             \tcena:   
'''

        for i in range(len(self.table_order_list)):
            if len(self.table_order_list[i]['nazov']) < 5:
                self.toFile += self.table_order_list[i]['nazov'] + '\t\t\t\t' + self.table_order_list[i]['cena'] + ' €\n'
            elif len(self.table_order_list[i]['nazov']) < 8:
                self.toFile += self.table_order_list[i]['nazov'] + '\t\t\t' + self.table_order_list[i]['cena'] + ' €\n'
            else:
                self.toFile += self.table_order_list[i]['nazov'] + '\t\t' + self.table_order_list[i]['cena'] + ' €\n'
        

        self.toFile += f'''------------------------------
platba :           \t{self.table_order_price.json()[0]['cena']} €
platba v hotovosti - akceptovaná
==============================
      
'''
        self.file1.write(self.toFile)

        self.file1.close()
        num += 1      
        print(num)  




    # methods for menu button, changing colour if cursor on the button
    def main_input(self, event):
        self.menu_button.configure(bg = "#3a7ca5")
    def main_output(self, event):
        self.menu_button.configure(bg = "white")

    # show and hide user informations
    def show_user(self, event):
        self.user_info_frame.place(x = 1075 ,y = 620)
        
    
    def hide_user(self, event):
        self.user_info_frame.place_forget()
