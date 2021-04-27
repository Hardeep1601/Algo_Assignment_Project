from tkinter import *
def TakeInput():
    if tb1.get() == tb2.get():
        print.tb1.get()
tk=Tk()

#Entry 1
tb1=Entry(tk)
tb1.pack()

#Entry 2
tb2=Entry(tk)
tb2.pack()

#Button
b=Button(tk,text="PrintInput",command= TakeInput)
b.pack()
tk.mainloop()