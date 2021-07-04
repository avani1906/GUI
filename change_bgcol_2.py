from tkinter import *

def funcA():
    v1=v.get()
    return l1.configure(bg=v1)
    
win=Tk()
win.geometry("280x250")

l=Label(win,text="Enter color name :")
l.grid(row=0,column=0)

v=StringVar()
e=Entry(win,textvariable=v)
e.grid(row=0,column=1)

l1=Listbox(win)
l1.grid(row=2,column=1,pady=30)

b1=Button(win,text="Enter",command=funcA)
b1.grid(row=1,column=1,pady=5,padx=5)

win.mainloop()