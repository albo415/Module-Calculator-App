#include mathlib
from tkinter import *
a = 0
b = 0
c=0
d=0
base= 0
modulo=0
esponente=0
risultato =0
def entry(numero):
    global a
    if(a==0):
       if(numero==0):
           return
    current = e.get()
    e.delete(0,END)
    e.insert(0,str(current) + str(numero))
    a=int(1)
    return

def equal():
    global modulo
    global risultato
    global d
    global c
    global b
    if(d==0 and b==1 and c==1 and e.get()!=int(0)):
        modulo = int(e.get())
        e.delete(0, END)
        risultato = pow(base, esponente, modulo)
        e.insert(0, str(risultato))
    b=int(0)
    c=int(0)
    return
def module():
    global esponente
    global c
    global b
    if(c==0 and b==1  and e.get()!=int(0)):
        esponente = int(e.get())
        e.delete(0, END)
        c = int(1)
    return
def power():
    global base
    global b
    if(b==0  and e.get()!=int(0)):
             base = int(e.get())
             e.delete(0, END)
             b=int(1)
    return
def cancel_all():
    e.delete(0,END)
    global b
    global c
    global d
    b = int(0)
    c = int(0)
    d = int(0)
    return
window = Tk()
window.title("MODULE CALCULATOR")
#window.iconbitmap("HACKER.ico")
window.geometry("517x370")
window.resizable("False","False")
window.configure(background='#eef5b3')

e = Entry(window, width=35, borderwidth=5,bg="#eef5b3",fg="#ed2d02")
e.grid(row=0,column=0,columnspan=5,padx=10,pady=10,rowspan=1)
button_7 = Button(window, text="7",padx=57,pady=20,command = lambda: entry(7),bg="#eef5b3",fg="#ed2d02")
button_8 = Button(window, text="8",padx=56,pady=20,command =  lambda: entry(8),bg="#eef5b3",fg="#ed2d02")
button_9 = Button(window, text="9",padx=57,pady=20,command =  lambda: entry(9),bg="#eef5b3",fg="#ed2d02")
button_4 = Button(window, text="4",padx=57,pady=20,command =  lambda: entry(4),bg="#eef5b3",fg="#ed2d02")
button_5 = Button(window, text="5",padx=55,pady=20,command =  lambda: entry(5),bg="#eef5b3",fg="#ed2d02")
button_6 = Button(window, text="6",padx=57,pady=20,command =  lambda: entry(6),bg="#eef5b3",fg="#ed2d02")
button_3 = Button(window, text="3",padx=57,pady=20,command =  lambda: entry(3),bg="#eef5b3",fg="#ed2d02")
button_2 = Button(window, text="2",padx=56,pady=20,command =  lambda: entry(2),bg="#eef5b3",fg="#ed2d02")
button_1 = Button(window, text="1",padx=58,pady=20,command =  lambda: entry(1),bg="#eef5b3",fg="#ed2d02")
button_0 = Button(window, text="0",padx=57,pady=20,command =  lambda: entry(0),bg="#eef5b3",fg="#ed2d02")
button_pow = Button(window, text="POWER",padx=39,pady=20,command = power,bg="#eef5b3",fg="#ed2d02")
button_mod = Button(window, text="MODULE",padx=39,pady=20,command = module,bg="#eef5b3",fg="#ed2d02")
button_eq = Button(window, text="=",padx=53,pady=55,command = equal,bg="#eef5b3",fg="#ed2d02")
button_AC = Button(window, text="CLEAR",padx=39,pady=56,command = cancel_all,bg="#eef5b3",fg="#ed2d02")
button_7.grid(row=1,column=0)
button_8.grid(row=1,column=1)
button_9.grid(row=1,column=2)
button_4.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2)
button_1.grid(row=3,column=0)
button_2.grid(row=3,column=1)
button_3.grid(row=3,column=2)
button_0.grid(row=4,column=0)
button_pow.grid(row=4,column=1)
button_mod.grid(row=4,column=2)
button_AC.grid(row=1,column=4,rowspan=2)
button_eq.grid(row=3,column=4,rowspan = 2)
etichetta1 = Label(window,text = "Attribution-NoDerivatives 4.0 International",fg="#ed2d02",bg="#eef5b3")
etichetta1.grid(row=5,column=0,columnspan=5)
etichetta2 = Label(window,text = "Creative Commons, created by Alberto Falciola",fg="#ed2d02",bg="#eef5b3")
etichetta2.grid(row=6,column=0,columnspan=5)
window.mainloop()