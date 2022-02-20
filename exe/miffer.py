from tkinter import *
from PIL import ImageTk, Image
from datetime import datetime
from tkinter import ttk
import requests
import os.path
import importlib
import time
import threading

root = Tk()
root.title("Miffer Caffe")
root.iconbitmap("D:/programovanie/PAJTON/tkinter ulohy/Miffer Caffe/mifferikona.ico")
root.configure(bg = '#006080')
root.geometry('1300x750')
root.resizable(False, False)
main_window = True
white_window = True

global save_path
save_path = 'D:/programovanie/PAJTON/tkinter ulohy/Miffer Caffe/blocky'
num = 1
global path_fr
path_fr = None


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
        self.shortage_label = Label(self.frame_orders, font = ('Helvetica', 10), fg = 'black', bg = '#e6ffff')


        # pointless stuff
        self.line = Canvas(self.frame, width = 650 , height = 5 , bg = "black", borderwidth = 0).place(relx = .12, rely = .32)
        self.user = Label(self.frame, text = f"User : {username.get().strip()}", bg = "white" , font = ("Helvetica", 10))
        self.user.place(x = 1150, y = 685)
        self.user.bind("<Enter>", self.show_user)
        self.user.bind("<Leave>", self.hide_user)
        
        

        #options
        self.options_picture = ImageTk.PhotoImage(Image.open("D:/programovanie/PAJTON/tkinter ulohy/Miffer Caffe 2/Miffer Caffe/settings_img.png"))
        self.options = Button(self.frame , image = self.options_picture, command = self.settings, bg = 'white', borderwidth = 3, relief = FLAT)
        self.options_frame = Frame (self.frame, bg = '#006080', relief = GROOVE, borderwidth = 2, height = 450, width = 350 )
        self.exit_options = Button(self.options_frame, bg = 'white', text = 'exit', command = self.close_opts, relief = FLAT)
        self.exit_options.place(relx = 0.8, rely = 0.9)
        self.path_label = Label (self.options_frame, text = 'Cesta pre ukladanie bločkov',font = ('Helvetica', 10), fg = 'white', bg = '#006080')
        self.path_label.place(x = 32, y = 15)
        self.path = Entry(self.options_frame, relief = FLAT, width = 23, font = ('Helvetica', 16))
        self.path.place(relx = 0.1, rely = 0.1)
        self.confirm_path = Button(self.options_frame, text = 'Confirm', bg = 'white', relief = FLAT, command = self.confirm_path_func)
        self.confirm_path.place(x = 260, y = 80)
        self.bad_path = Label(self.options_frame, text = 'Táto cesta nie je validná', bg = '#006080', fg = 'white')

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
            self.shortage_string = 'Tovar \t\t\t\t Množstvo\n----------------------------------------------------------\n'
            self.shortage = requests.get('http://localhost/getnedostatok.php')
            self.shortage_js = self.shortage.json()
            for i in range(len(self.shortage_js)):
                self.shortage_string += self.shortage_js[i]['nazov'] + '\t\t\t\t' + self.shortage_js[i]['mnozstvo'] + '\n'
            self.shortage_label.config(text = self.shortage_string)
            self.frame_orders.place(relx = .12 , rely = .4)
            self.info_orders.place(relx = .12 , rely = .35)
            self.shortage_label.place(x = 45, y = 15)
            self.options.place(x = 60, y = 670)
            main_window = False
        else:
            self.shortage_string = 'Tovar \t\t\t\t  Počet na sklade\n\n'
            self.info_orders.place_forget()
            self.frame_orders.place_forget()
            self.options.place_forget()
            main_window = True
        self.shortage_string = ''


    def confirm_path_func(self):
        global path_fr
        def_path = self.path.get().strip()
        if os.path.isdir(def_path):
            path_fr = def_path
            self.bad_path.place_forget()
            self.exit_options.place(relx = 0.8, rely = 0.9)
        else:
            self.exit_options.place_forget()
            for i in range(len(self.tables)):
                self.tables[i].place_forget()
            self.bad_path.place(x = 35, y = 85)


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
        self.table_order = requests.post('http://localhost/getstol.php', json={'id_stol': args + 1})
        self.table_order_list = self.table_order.json()
        self.table_order_string = '\n'

        self.count = 0

        global pay_intro, pay, pay_w_cash
        # payment
        pay_intro = Label(self.new_frame, text = 'Zaplatiť : ', fg = "black", bg = 'white', font = ("Arial", 8))
        pay = Button(self.new_frame, text = 'Karta', relief = FLAT, bg = "#006080", fg = "white", command =lambda: self.pay(args, self.count))
        pay_w_cash = Button(self.new_frame, text = 'Hotovosť', relief = FLAT, bg = "#006080", fg = "white", command = lambda: self.pay_cash(args, self.count))


        #frame for orders with scrollbar


        self.scroll_frame = Frame(self.new_frame, width = 50, height = 50)
        self.scroll_frame.place(x = 75, y = 95)

        self.scrollbar = Scrollbar(self.scroll_frame)
        self.scrollbar.pack(side='right', fill='y')

        self.listbox = ttk.Treeview(self.scroll_frame, selectmode='browse', yscrollcommand= self.scrollbar.set)
        # load the listbox


        self.treew(args, self.count)
        



      

        if len(self.table_order_list) != 0:
            pay_intro.place(x = 360, y = 330)
            pay.place(x = 445, y = 330)
            pay_w_cash.place(x = 445, y = 360)

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


        

        
    def treew(self, args, count):
        global pay_intro, pay, pay_w_cash
        self.table_order = requests.post('http://localhost/getstol.php', json={'id_stol': args + 1})
        self.table_order_list = self.table_order.json()

        

        if self.count == 0:
            for i in range(len(self.table_order_list)):
                if self.table_order_list[i]['stav'] == "1":
                    self.listbox.insert("",'end',text="L1",values=(self.table_order_list[i]['nazov'], self.table_order_list[i]['cena'] + ' €', self.order_comment(self.table_order_list[i]['poznamka']), 'Vybavené'))
                    self.count += 1
                    pay_intro.place(x = 360, y = 330)
                    pay.place(x = 445, y = 330)
                    pay_w_cash.place(x = 445, y = 360)
                else:
                    self.listbox.insert("",'end',text="L1",values=(self.table_order_list[i]['nazov'], self.table_order_list[i]['cena'] + ' €', self.order_comment(self.table_order_list[i]['poznamka']), 'Objednané'))
                    self.count += 1
                    pay_intro.place(x = 360, y = 330)
                    pay.place(x = 445, y = 330)
                    pay_w_cash.place(x = 445, y = 360)
        
        elif self.count < len(self.table_order_list):
            for _ in range(len(self.table_order_list) - self.count):
                if self.table_order_list[self.count -1]['stav'] == "1":
                    self.listbox.insert("",'end',text="L1",values=(self.table_order_list[self.count]['nazov'], self.table_order_list[self.count -1]['cena'] + ' €', self.order_comment(self.table_order_list[self.count -1]['poznamka']), 'Vybavené'))
                    self.count += 1
                    pay_intro.place(x = 360, y = 330)
                    pay.place(x = 445, y = 330)
                    pay_w_cash.place(x = 445, y = 360)
                else:
                    self.listbox.insert("",'end',text="L1",values=(self.table_order_list[self.count]['nazov'], self.table_order_list[self.count -1]['cena'] + ' €', self.order_comment(self.table_order_list[self.count -1]['poznamka']), 'Objednané'))
                    self.count += 1
                    pay_intro.place(x = 360, y = 330)
                    pay.place(x = 445, y = 330)
                    pay_w_cash.place(x = 445, y = 360)

        try:
           for item in self.prev_list:
                if item not in self.table_order_list:
                    for i in self.listbox.get_children():
                        self.listbox.delete(i)
                        self.count = 0
                        
        except:
            pass
            

        self.listbox.pack()
        self.scrollbar.config(command=self.listbox.yview)
        self.table_order_price = requests.post('http://localhost/getcena.php', json={'stol': args + 1})
        if self.table_order_price.json()[0]['cena'] != None:
            self.order_price = Label(self.new_frame, text = f"Cena spolu : {self.table_order_price.json()[0]['cena']} €" , bg = 'white', justify = LEFT)
            self.order_price.place(x = 75, y = 330)
        else:
            self.order_price = Label(self.new_frame, text = f"Cena spolu : 0 €      " , bg = 'white', justify = LEFT)
            self.order_price.place(x = 75, y = 330)

        self.prev_list = self.table_order.json()

        

        threading.Timer(1, lambda : self.treew(args, count)).start()
        
        if not self.new_window.winfo_exists():
            threading.Timer(1, lambda : self.treew(args, count)).cancel()
            return
    

    def settings(self):
        self.options_frame.place(relx=0.5, rely=0.5, anchor=CENTER)

    def close_opts(self):
        self.options_frame.place_forget()
        for i in range(len(self.tables)):
            self.tables[i].place(relx = .7, rely = .23 + float(i/9))


    # order comment function
    def order_comment(self, order_compare):
        if order_compare == "":
            return "-"
        else:
            return order_compare


    # card pay method
    def pay(self, args, count):
        global num
        global pay_intro, pay, pay_w_cash
        if self.table_order_price.json()[0]['cena'] != None:
            if path_fr == None:
                self.completeName = os.path.join(save_path, f'blocek {num}.txt')
            else:
                self.completeName = os.path.join(path_fr, f'blocek {num}.txt')
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
            self.paid_dict = {  'id_stol' : args + 1, 
                            'cena' : self.table_order_price.json()[0]['cena']
            }
            self.paid = requests.post('http://localhost/dokoncenieobjednavky.php', json = self.paid_dict)
            self.count = 0

            for selected_item in self.listbox.get_children():
                self.listbox.delete(selected_item)

            self.order_price.place_forget()

            pay.place_forget()
            pay_w_cash.place_forget()
            pay_intro.place_forget()
            self.order_price.place_forget()

    # cash pay method 
    def pay_cash(self, args, count):
        global num
        if path_fr == None:
            self.completeName = os.path.join(save_path, f'blocek {num}.txt')
        else:
            self.completeName = os.path.join(save_path, f'blocek {num}.txt')

        self.now = datetime.now()
        self.time = self.now.strftime('%d.%m.%Y')
        self.hours = self.now.strftime("%H:%M")
        

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
platba v hotovsti - akceptovaná
dňa - {self.time}    {self.hours}
==============================
      
'''
        self.file1.write(self.toFile)

        self.file1.close()
        num += 1 
        self.count = 0
        self.paid_dict = {  'id_stol' : args + 1, 
                            'cena' : self.table_order_price.json()[0]['cena']
            }
        self.paid = requests.post('http://localhost/dokoncenieobjednavky.php', json = self.paid_dict)
        self.count = 0

        for selected_item in self.listbox.get_children():
            self.listbox.delete(selected_item)

        self.order_price.place_forget()

        pay.place_forget()
        pay_w_cash.place_forget()
        pay_intro.place_forget()


        for selected_item in self.listbox.get_children():
            self.listbox.delete(selected_item)


        self.order_price.place_forget()
        pay.place_forget()
        pay_w_cash.place_forget()
        pay_intro.place_forget()


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


# methods for table button, changing colour if cursor on the button
def inputt(event):
    event.widget.config(bg="#3a7ca5")  
def output(event):
    event.widget.config(bg="#006080")



def submit():
    global log_user
    log_user = username.get().strip()
    log_pass = password.get().strip()
    root_set = requests.post('http://localhost/login.php', json =  {'prihlasovacie_meno': log_user, 'heslo': log_pass})
    try:
        if root_set.json()[0]['meno'] == log_user:
            #delete login widgets 
            global time
            now = datetime.now()
            time = now.strftime("%H:%M")
            ram.pack_forget()
            #show the main window
            display = Plocha(root)
    except TypeError:
        war.place(x = 450, y = 400)

            


            
# login frames   
ram = Frame(root, width = 3000 , height = 1200 , bg = "white", borderwidth = 0)
ram.pack(pady = 40, padx = 60)
log_ram = Canvas(ram, width = 370, height = 220, bg = "#006080", borderwidth = 2, relief = GROOVE)
log_ram.place(x = 420, y = 230)




# miffer texts
miffer_login = []
miffer_welc = Label(ram, text = "MIFFER CAFFE", fg = "white", bg = "#006080", font = ("Book Antiqua", 12))
miffer_welc.place(x = 440, y = 250)
username_prompt = Label(ram, text = "Prihlasovacie meno :", fg = "white", bg = '#006080', font = ("Arial", 8))
username_prompt.place(x = 450, y = 280)
password_prompt = Label(ram, text = "Heslo :", fg = "white", bg = '#006080', font = ("Arial", 8))
password_prompt.place(x = 450, y = 325)
war = Label(ram, text = "oops, zadal si niečo zlé, skús to znova ", fg = "red", bg = '#006080', font = ("Arial", 12, 'bold'))


# entry fields 
password = Entry(ram, show = "*", relief = FLAT)
password.place(x = 450, y = 345)
username = Entry(ram, relief = FLAT)
username.place(x = 450, y = 300)
submit = Button(ram, text = "Submit", relief = FLAT, bg = "white", command = submit)
submit.place(x = 525, y = 370)



root.mainloop()