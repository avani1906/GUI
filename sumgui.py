from tkinter import *

def sum():
    n11=n1.get()
    n22=n2.get()
    n=n11+n22
    a="your answer is "+str(n)
    return l.config(text=a)




win=Tk()
win.title("SUM WINDOW")

l1=Label(win,text="SUM")
l1.grid(row=0,column=2)

l2=Label(win,text="First number :")
l2.grid(row=2,column=1)

n1=IntVar()
e1=Entry(win,textvariable=n1)
e1.grid(row=2,column=2)

l3=Label(win,text="Last number :")
l3.grid(row=3,column=1)

n2=IntVar()
e2=Entry(win,textvariable=n2)
e2.grid(row=3,column=2)

b=Button(win,text="Submit",command=sum)
b.grid(row=4,column=2)

l=Label(win)
l.grid(row=5,column=2)





win.mainloop()