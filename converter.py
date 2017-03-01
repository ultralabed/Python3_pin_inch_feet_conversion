import tkinter as tk
from tkinter import ttk
from tkinter import StringVar
from tkinter import messagebox
from tkinter import OptionMenu

window=tk.Tk()
lan = StringVar(window)
lan.set("中文") # default value

calfootage2="坪" if lan.get() == '中文' else "Square footage"
calmeter2="平方公尺" if lan.get() == '中文' else "Square meters"
calfeet2="平方英呎" if lan.get() == '中文' else "Square feets"
converBtn="轉換" if lan.get() == '中文' else "convert"
title="面積換算器" if lan.get() == '中文' else "Transformation Area Converter"
warningMsg="請填入至少一個數字" if lan.get() == '中文' else "Please enter at least one number for convertion"

window.title(title)
window.geometry('430x115+30+0')
window.resizable(False, False)
eleWidth=14
eleEntryWidth=16

def changeLan(self):
    l1["text"]=calfootage2="坪" if lan.get() == '中文' else "Square footage"
    l2["text"]=calmeter2="平方公尺" if lan.get() == '中文' else "Square meters"
    l3["text"]=calfeet2="平方英呎" if lan.get() == '中文' else "Square feets"
    b1["text"]=b2["text"]=b3["text"]=converBtn="轉換" if lan.get() == '中文' else "convert"
    title="面積換算器" if lan.get() == '中文' else "Converter"
    global warningMsg
    warningMsg="請填入至少一個數字" if lan.get() == '中文' else "Please enter at least one number for convertion"
    window.title(title)

def convert_square_footage():
    if(e1_value.get() != ''):
        feets=round(float(e1_value.get())*35.583185317, 3)
        e3.delete(0, tk.END)
        e3.insert(0, feets)

        m2=round(float(e1_value.get())*3.3057862168, 3)
        e2.delete(0, tk.END)
        e2.insert(0, m2)
    else:
        messagebox.showinfo(message=warningMsg)

def convert_square_meters():
    if(e2_value.get() != ''):
        feets=round(float(e2_value.get())*10.76391, 3)
        e3.delete(0, tk.END)
        e3.insert(0, feets)

        pin=round(float(e2_value.get())*0.3024999, 3)
        e1.delete(0, tk.END)
        e1.insert(0, pin)
    else:
        messagebox.showinfo(message=warningMsg)

def convert_square_feets():
    if(e3_value.get() != ''):
        m2=round(float(e3_value.get())*0.0929030436, 3)
        e2.delete(0, tk.END)
        e2.insert(0, m2)

        pin=round(float(e3_value.get())*0.0281031614, 3)
        e1.delete(0, tk.END)
        e1.insert(0, pin)
    else:
        messagebox.showinfo(message=warningMsg)

l1=tk.Label(window, text=calfootage2, width=eleWidth, anchor='w')
l1.grid(row=2, column=0, padx=10)

e1_value=tk.StringVar()
e1=tk.Entry(window, textvariable=e1_value, width=eleEntryWidth)
e1.grid(row=2, column=1)

b1=tk.Button(window, text=converBtn, command=convert_square_footage, width=eleWidth)
b1.grid(row=2, column=2)

l2=tk.Label(window, text=calmeter2, width=eleWidth, anchor='w')
l2.grid(row=3, column=0)

e2_value=tk.StringVar()
e2=tk.Entry(window, textvariable=e2_value, width=eleEntryWidth)
e2.grid(row=3, column=1)

b2=tk.Button(window, text=converBtn, command=convert_square_meters, width=eleWidth)
b2.grid(row=3, column=2)

l3=tk.Label(window, text=calfeet2, width=eleWidth, anchor='w')
l3.grid(row=4, column=0)

e3_value=tk.StringVar()
e3=tk.Entry(window, textvariable=e3_value, width=eleEntryWidth)
e3.grid(row=4, column=1)

b3=tk.Button(window, text=converBtn, command=convert_square_feets, width=eleWidth)
b3.grid(row=4, column=2)

l4=tk.Label(window, text='Made by Ed Shih', width=eleWidth)
l4.grid(row=5, column=2)

dropdown0 = OptionMenu(window, lan, "English", "中文", command=changeLan)
dropdown0.grid(row=5, column=0, sticky="w")

window.mainloop()
