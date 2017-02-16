import tkinter as tk
from tkinter import ttk
from tkinter import StringVar

window=tk.Tk()

lan='english'


calfootage2="坪" if lan == 'chinese' else "Square footage"
calmeter2="平方公尺" if lan == 'chinese' else "Square meters"
calfeet2="平方英呎" if lan == 'chinese' else "Square feets"
converBtn="轉換" if lan == 'chinese' else "convert"
language="語系" if lan == 'chinese' else "Language"
lanBtnEn="英文" if lan == 'chinese' else "English"
lanBtnCh="中文" if lan == 'chinese' else "Chinese"

def changeLan():
    l0["text"]=l5["text"]=l8["text"]=calfootage2="坪" if lan == 'chinese' else "Square footage"
    l2["text"]=l3["text"]=l7["text"]=calmeter2="平方公尺" if lan == 'chinese' else "Square meters"
    l1["text"]=l4["text"]=l6["text"]=calfeet2="平方英呎" if lan == 'chinese' else "Square feets"
    b0["text"]=b3["text"]=b6["text"]=converBtn="轉換" if lan == 'chinese' else "convert"
    l9["text"]=language="語系" if lan == 'chinese' else "Language"
    btnEnglish["text"]=lanBtnEn="英文" if lan == 'chinese' else "English"
    btnChinese["text"]=lanBtnCh="中文" if lan == 'chinese' else "Chinese"

def convert_pin():
    pin_to_feets()
    pin_to_square_meters()

def pin_to_feets():
    inch2=round(float(e1_value.get())*35.587, 3)
    t1.delete('1.0', tk.END)
    t1.insert(tk.END, inch2)

def pin_to_square_meters():
    m2=round(float(e1_value.get())*3.305, 3)
    t2.delete('1.0', tk.END)
    t2.insert(tk.END, m2)

b0=tk.Button(window, text=converBtn, command=convert_pin)
b0.grid(row=0, column=2)

l0=tk.Label(window, text=calfootage2)
l0.grid(row=0, column=0)

e1_value=tk.StringVar()
e1=tk.Entry(window, textvariable=e1_value)
e1.grid(row=0, column=1)

l1=tk.Label(window, text=calfeet2)
l1.grid(row=1, column=0)
t1=tk.Text(window, height=1, width=20)
t1.grid(row=1, column=1)

l2=tk.Label(window, text=calmeter2)
l2.grid(row=2, column=0)
t2=tk.Text(window, height=1, width=20)
t2.grid(row=2, column=1)

ttk.Separator(window,orient='horizontal').grid(row=3, columnspan=3, sticky="ew")

# Conver square_meters_to_feets_and_pin
def convert_m2():
    m2_to_feets()
    m2_to_pin()

def m2_to_feets():
    inch2=round(float(e3_value.get())*10.76, 3)
    t4.delete('1.0', tk.END)
    t4.insert(tk.END, inch2)

def m2_to_pin():
    pin=round(float(e3_value.get())/3.305, 3)
    t5.delete('1.0', tk.END)
    t5.insert(tk.END, pin)

b3=tk.Button(window, text=converBtn, command=convert_m2)
b3.grid(row=4, column=2)

l3=tk.Label(window, text=calmeter2)
l3.grid(row=4, column=0)

e3_value=tk.StringVar()
e3=tk.Entry(window, textvariable=e3_value)
e3.grid(row=4, column=1)

l4=tk.Label(window, text=calfeet2)
l4.grid(row=5, column=0)
t4=tk.Text(window, height=1, width=20)
t4.grid(row=5, column=1)

l5=tk.Label(window, text=calfootage2)
l5.grid(row=6, column=0)
t5=tk.Text(window, height=1, width=20)
t5.grid(row=6, column=1)

ttk.Separator(window,orient='horizontal').grid(row=7, columnspan=3, sticky="ew")

# Conver feet2_to_m2_and_pin
def convert_feets():
    feets_to_m2()
    feets_to_pin()

def feets_to_m2():
    m2=round(float(e6_value.get())*0.093, 3)
    t7.delete('1.0', tk.END)
    t7.insert(tk.END, m2)

def feets_to_pin():
    pin=round(float(e6_value.get())/35.587, 3)
    t8.delete('1.0', tk.END)
    t8.insert(tk.END, pin)

b6=tk.Button(window, text=converBtn, command=convert_feets)
b6.grid(row=8, column=2)

l6=tk.Label(window, text=calfeet2)
l6.grid(row=8, column=0)

e6_value=tk.StringVar()
e6=tk.Entry(window, textvariable=e6_value)
e6.grid(row=8, column=1)

l7=tk.Label(window, text=calmeter2)
l7.grid(row=9, column=0)
t7=tk.Text(window, height=1, width=20)
t7.grid(row=9, column=1)

l8=tk.Label(window, text=calfootage2)
l8.grid(row=10, column=0)
t8=tk.Text(window, height=1, width=20)
t8.grid(row=10, column=1)

ttk.Separator(window,orient='horizontal').grid(row=11, columnspan=3, sticky="ew")

def chagneLanEn():
    global lan
    lan='english'
    changeLan()

def chagneLanCh():
    global lan
    lan='chinese'
    changeLan()

l9=tk.Label(window, text=language)
l9.grid(row=12, column=0)
btnEnglish=tk.Button(window, text=lanBtnEn, command=chagneLanEn)
btnEnglish.grid(row=12, column=1)
btnChinese=tk.Button(window, text=lanBtnCh, command=chagneLanCh)
btnChinese.grid(row=12, column=2)

window.mainloop()
