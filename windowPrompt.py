# Reference
# https://datatofish.com/entry-box-tkinter/
# https://stackoverflow.com/questions/7727804/tkinter-using-scrollbars-on-a-canvas

import tkinter as tk
from tkinter import *

root= tk.Tk()
# Create frame
frame=Frame(root,width=300,height=300)
frame.pack(expand=True, fill=BOTH) #.grid(row=0,column=0)
canvas1=Canvas(frame,bg='#FFFFFF',width=300,height=300,scrollregion=(0,0,500,500))

# Create canvas
# canvas1 = tk.Canvas(root, width = 400, height = 600,  relief = 'raised')
canvas1.pack()
# Add entry box
label1 = tk.Label(root, text='Calculate the Square Root')
label1.config(font=('helvetica', 14))



canvas1.create_window(300, 25, window=label1)
label2 = tk.Label(root, text='Type your Number:')
label2.config(font=('helvetica', 10))
canvas1.create_window(300, 100, window=label2)

entry1 = tk.Label(root, text="EmployeeID:").grid(row=0)
entry2 = tk.Label(root, text="Employee Name").grid(row=1)
e = tk.Entry(root)
en = tk.Entry(root)
e.grid(row=0, column=1)
en.grid(row=1, column=1)

# # Origin
# entry1 = tk.Entry (root)
canvas1.create_window(300, 140, window=entry1)
canvas1.create_window(300, 140, window=entry2)


def getSquareRoot ():
    x1 = entry1.get()
    label3 = tk.Label(root, text= 'The Square Root of ' + x1 + ' is:',font=('helvetica', 10))
    canvas1.create_window(300, 210, window=label3)
    label4 = tk.Label(root, text= float(x1)**0.5,font=('helvetica', 10, 'bold'))
    canvas1.create_window(300, 230, window=label4)


button1 = tk.Button(text='Get the Square Root', command=getSquareRoot, bg='brown', fg='white', font=('helvetica', 9, 'bold'))
canvas1.create_window(300, 180, window=button1)


canvas1.config(width=600,height=400)



root.mainloop()


# root= tk.Tk()
# # Create frame
# frame=Frame(root,width=300,height=300)
# frame.pack(expand=True, fill=BOTH) #.grid(row=0,column=0)
# canvas1=Canvas(frame,bg='#FFFFFF',width=300,height=300,scrollregion=(0,0,500,500))
#
# # Create canvas
# # canvas1 = tk.Canvas(root, width = 400, height = 600,  relief = 'raised')
# canvas1.pack()
# # Add entry box
# label1 = tk.Label(root, text='Calculate the Square Root')
# label1.config(font=('helvetica', 14))
#
#
#
# canvas1.create_window(200, 25, window=label1)
# label2 = tk.Label(root, text='Type your Number:')
# label2.config(font=('helvetica', 10))
# canvas1.create_window(200, 100, window=label2)
# entry1 = tk.Entry (root)
# canvas1.create_window(200, 140, window=entry1)
#
# def getSquareRoot ():
#     x1 = entry1.get()
#     label3 = tk.Label(root, text= 'The Square Root of ' + x1 + ' is:',font=('helvetica', 10))
#     canvas1.create_window(200, 210, window=label3)
#     label4 = tk.Label(root, text= float(x1)**0.5,font=('helvetica', 10, 'bold'))
#     canvas1.create_window(200, 230, window=label4)
#
#
# button1 = tk.Button(text='Get the Square Root', command=getSquareRoot, bg='brown', fg='white', font=('helvetica', 9, 'bold'))
# canvas1.create_window(200, 180, window=button1)
#
# # Vertical bar
# vbar=Scrollbar(frame,orient=VERTICAL)
# vbar.pack(side=RIGHT,fill=Y)
# vbar.config(command=canvas1.yview)
#
# canvas1.config(width=600,height=800)
# canvas1.config(yscrollcommand=vbar.set)
# canvas1.pack(side=LEFT,expand=True,fill=BOTH)
#
#
# root.mainloop()
