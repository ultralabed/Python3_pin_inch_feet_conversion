import tkinter as tk

window=tk.Tk()

def convert_pin():
    pin_to_inches()
    pin_to_square_meters()

def pin_to_inches():
    inch2=float(e1_value.get())*35.583
    t1.delete('1.0', tk.END)
    t1.insert(tk.END, inch2)

def pin_to_square_meters():
    m2=float(e1_value.get())*3.3058
    t2.delete('1.0', tk.END)
    t2.insert(tk.END, m2)

b0=tk.Button(window, text="轉換", command=convert_pin)
b0.grid(row=0, column=2)

l0=tk.Label(window, text="坪")
l0.grid(row=0, column=0)

e1_value=tk.StringVar()
e1=tk.Entry(window, textvariable=e1_value)
e1.grid(row=0, column=1)

l1=tk.Label(window, text="平方英呎")
l1.grid(row=1, column=0)
t1=tk.Text(window, height=1, width=20)
t1.grid(row=1, column=1)

l2=tk.Label(window, text="平方公尺")
l2.grid(row=2, column=0)
t2=tk.Text(window, height=1, width=20)
t2.grid(row=2, column=1)

window.mainloop()
