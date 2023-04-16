from tkinter import *

def show():
    global e1,user
    print(e1.get())
    

def login():
    global e1,user
    log=Toplevel()
    l1=Label(log,text="Username : ").grid(row=0,column=0)
    user=StringVar
    e1=Entry(log,textvariable=user)
    e1.grid(row=0,column=1)
    but=Button(log,text="show",command=show).grid(row=1,column=0)
    log.mainloop()

def signup():
    sign=Toplevel()
    sign.mainloop()

root=Tk()
root.geometry("500x500")
b1=Button(root, text="login",command=login).pack()
b2=Button(root, text="Signup",command=signup).pack()
root.mainloop()