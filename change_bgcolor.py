from tkinter import *
def red():
    return l1.configure(bg="red")

def blue():
    return l1.configure(bg="blue")

def pink():
    return l1.configure(bg="pink")
win=Tk()
win.geometry("280x250")

b1=Button(win,text="___Red___",bg="red",command=red)
b1.grid(row=0,column=1,pady=10,padx=10)

b2=Button(win,text="___Blue___",bg="blue",command=blue)
b2.grid(row=0,column=2,pady=10)

b3=Button(win,text="___Pink___",bg='pink',command=pink)
b3.grid(row=0,column=3,pady=10)

l1=Listbox(win)
l1.grid(row=1,column=2,pady=20)

win.mainloop()

