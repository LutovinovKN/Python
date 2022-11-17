from tkinter import *
from tkinter import ttk
root = Tk()
frm = ttk.Frame(root, padding=10) # отступы
frm.grid()
ttk.Label(frm, text="Hello World!").grid(column=1, row=2)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=2, row=3)
root.mainloop()