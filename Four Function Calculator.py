import math
from tkinter import * 
from tkinter import messagebox 
top = Tk() 
top.geometry("700x300")
L1 = Label(top, text="Number 1") 
L1.pack( side = LEFT) 
E1 = Entry(top, bd =3) 
E1.pack(side = LEFT)

L2 = Label(top, text="Number 2") 
L2.pack( side = LEFT) 
E2 = Entry(top, bd =3) 
E2.pack(side = LEFT)


L3 = Label(top, text="Enter This for sin/cos op") 
L3.pack( side = LEFT) 
E3 = Entry(top, bd =3) 
E3.pack(side = LEFT)


def Add(): 
   msg=messagebox.showinfo( "Add", int(E1.get())+int(E2.get())) 
B = Button(top, text ="Add", command = Add) 
B.place(x=240,y=250)


def subtract(): 
    try:
        msg=messagebox.showinfo( "Subtract", int(E1.get())-int(E2.get()))
    except:
        msg=messagebox.showinfo( "Subtract", '0')
    
C = Button(top, text ="Subtract", command = subtract) 
C.place(x=100,y=250)



def Multiply(): 
   msg=messagebox.showinfo( "Multiply", int(E1.get())*int(E2.get())) 
D = Button(top, text ="Multipy", command =Multiply) 
D.place(x=150,y=250)



def Divide(): 
   msg=messagebox.showinfo( "Divide", int(E1.get())/int(E2.get())) 
E= Button(top, text ="Divide", command = Divide) 
E.place(x=200,y=250)




def sin(): 
   msg=messagebox.showinfo( "Sin", math.sin(int(E3.get()))) 
F = Button(top, text ="Sin", command = sin) 
F.place(x=240,y=200)

def Cos(): 
   msg=messagebox.showinfo( "Cos",math.cos(int(E3.get())) ) 
G = Button(top, text ="Cos", command = Cos) 
G.place(x=200,y=200)

def Tan(): 
   msg=messagebox.showinfo( "Tan", math.tan(int(E3.get()))) 
H = Button(top, text ="Tan", command = Tan) 
H.place(x=160,y=200)
top.mainloop()
