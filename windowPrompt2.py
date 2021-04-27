import tkinter as tk
from tkinter import *

class Window:

    numOfCustomer = 0

    def storeNum(self):
        # hold = box.get()
        print("Test"+int(str())+"...")



    def inputCustomer_1(self):
        # Number of customer

        first = tk.Tk()
        # str = 'Customer ' + int.__str__(i + 1) + ' Details'
        first.title("Customer Details")
        tk.Label(first, text='State the number of customers').grid(row=0, column=1)
        tk.Label(first, text="Customer Count: ").grid(row=1)

        # button widget
        b1 = Button(first, text="Submit", command=self.storeNum()).grid(row=3, column=1, sticky=E)

        # type box
        box = tk.Entry(first)
        box.grid(row=1, column=1)
        hold=box.get()
        first.mainloop()
        # self.numOfCustomer=int(str(box.get()))


        # Get the origin and destination for each customer
        # self.storeNum()
        for i in range(int(self.numOfCustomer)):
            first = tk.Tk()
            str='Customer '+int.__str__(i+1)+' Details'
            first.title("Customer Details")
            tk.Label(first, text=str).grid(row=0, column=1)
            tk.Label(first, text="Origin: ").grid(row=1)
            tk.Label(first, text="Destination: ").grid(row=2)

            # button widget
            b1 = Button(first, text="Submit").grid(row=3, column=1,sticky = E)

            e = tk.Entry(first)
            en = tk.Entry(first)
            e.grid(row=1, column=1)
            en.grid(row=2, column=1)
            first.mainloop()


        root = tk.Tk()
        # Create frame
        frame = Frame(root, width=300, height=300)
        frame.pack(expand=True, fill=BOTH)  # .grid(row=0,column=0)
        canvas1 = Canvas(frame, bg='#FFFFFF', width=300, height=300, scrollregion=(0, 0, 500, 500))

        # Create canvas
        # canvas1 = tk.Canvas(root, width = 400, height = 600,  relief = 'raised')
        canvas1.pack()


        root.title("Customer Input")
        label1 = tk.Label(root, text='Calculate the Square Root')
        label1.config(font=('helvetica', 14))
        canvas1.create_window(200, 25, window=label1)
        label2 = tk.Label(root, text='Type your Number:')
        button1 = tk.Button(text='Get the Square Root', command='storeNum()', bg='brown', fg='white',
                                font=('helvetica', 9, 'bold'))
        canvas1.create_window(900, 500, window=button1)
        canvas1.config(width=600, height=600)
        root.mainloop()



    def run(self):
        self.root.mainloop()

prompt = Window()
print(prompt.numOfCustomer)

prompt.storeNum()
print(prompt.numOfCustomer)
prompt.inputCustomer_1()
