import model
from tkinter import *
from tkinter import ttk

root = None
frm = None

def create_menu():
    global root
    global frm
    root = Tk()
    root.title("Phonebook")
    frm = ttk.Frame(root, padding = 10) # отступы
    frm.grid()
    ttk.Label(frm, text='''
                            Вы в главном меню
                            Выберите действие:
                        ''' ).pack(anchor="w")
    btn_open_all = ttk.Button(frm, text="Открыть список контактов", command=root.destroy)
    # btn_open_all.grid(column=1, row=3)
    btn_open_all.pack(anchor="w", padx=20, pady=30)
    
    btn_add_contact = ttk.Button(frm, text="Создать контакт", command=root.destroy)
    # btn_add_contact.grid(column=1, row=4)
    btn_add_contact.pack(anchor="w", padx=20, pady=31)
    
    btn_del_contact = ttk.Button(frm, text="Удалить контакт", command=root.destroy)
    # btn_del_contact.grid(column=1, row=5)
    btn_del_contact.pack(anchor="w", padx=20, pady=32)
    
    btn_exit = ttk.Button(frm, text="Quit", command=root.destroy)
    # btn_exit.grid(column=2, row=10)
    btn_exit.pack(anchor="se")
    root.mainloop()

def add_contact():
    global root
    global frm
    root = Tk()
    root.title("Phonebook")
    frm = ttk.Frame(root, padding = 10) # отступы
    frm.grid()
    ttk.Label(frm, text='''
                            Создайте контакт
                            Выберите действие:
                        ''' ).pack(anchor="w")
    btn_name = ttk.Button(frm, text="Задайте имя", command=root.destroy)
    # btn_name.grid(column=1, row=3)
    btn_name.pack(anchor="w", padx=20, pady=30)
    
    btn_surname = ttk.Button(frm, text="Задайте фамилию", command=root.destroy)
    # btn_surname.grid(column=1, row=4)
    btn_surname.pack(anchor="w", padx=20, pady=31)
    
    btn_number = ttk.Button(frm, text="Задайте номер телефона", command=root.destroy)
    # btn_number.grid(column=1, row=5)
    btn_number.pack(anchor="w", padx=20, pady=32)
    
    btn_number_work = ttk.Button(frm, text="Задайте рабочий номер телефона", command=root.destroy)
    # btn_number_work.grid(column=1, row=5)
    btn_number_work.pack(anchor="w", padx=20, pady=33)
    
    btn_exit = ttk.Button(frm, text="Quit", command=root.destroy)
    # btn_exit.grid(column=2, row=10)
    btn_exit.pack(anchor="se")
    root.mainloop()