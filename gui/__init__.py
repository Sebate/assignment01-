import tkinter as tk
from util import DistanceCalculator
from tkinter.messagebox import *

ed = DistanceCalculator()


def Show_results():
    sResult = (ed.distance(e1.get(), e2.get()))
    tk.messagebox.showinfo(title="Your Edit distance", message=sResult)


myForm = tk.Tk()
tk.Label(myForm, text="Enter 1st word").grid( row=0)
tk.Label(myForm, text="Enter 2nd word").grid( row=2)

e1 = tk.Entry(myForm)
e2 = tk.Entry(myForm)
e1.grid(row=0, column=1)
e2.grid(row=2, column=1)

tk.Button(myForm, text='Calculate', command=Show_results).grid(row=4, column=0, sticky=tk.W, pady=4)
tk.Button(myForm, text='Exit', command=myForm.quit).grid(row=4, column=1, sticky=tk.W, pady=4)
tk.mainloop()
