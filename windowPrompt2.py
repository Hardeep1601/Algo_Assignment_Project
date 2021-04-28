import tkinter as tk
from tkinter import *

class Window:

    numOfCustomer = 0
    originArr = []
    destinationArr = []


    def inputCustomer(self):
        # Number of customer

        first = tk.Tk()
        first.title("Customer Details")
        tk.Label(first, text='State the number of customers').grid(row=0, column=1)
        tk.Label(first, text="Customer Count: ").grid(row=1)


        # type box
        box = tk.Entry(first)
        box.grid(row=1, column=1)


        def saveCustNum():
            hold=box.get()
            self.numOfCustomer = hold
            first.destroy()

        # button widget
        b1 = Button(first, text="Submit", command=saveCustNum).grid(row=3, column=1, sticky=E)

        first.mainloop()



        # Get the origin and destination for each customer
        # self.storeNum()
        for i in range(int(self.numOfCustomer)):
            first = tk.Tk()
            str='Customer '+int.__str__(i+1)+' Details'
            first.title("Customer Details")
            tk.Label(first, text=str).grid(row=0, column=1)
            tk.Label(first, text="Origin: ").grid(row=1)
            tk.Label(first, text="Destination: ").grid(row=2)


            origin = tk.Entry(first)
            dest = tk.Entry(first)
            origin.grid(row=1, column=1)
            dest.grid(row=2, column=1)

            def saveCustDetail():
                self.originArr.append(origin.get())
                self.destinationArr.append(dest.get())
                first.destroy()

            # button widget
            b1 = Button(first, text="Submit", command=saveCustDetail).grid(row=3, column=1,sticky = E)
            first.mainloop()


    # Create output window for program
    def ouputWindow(self):
        root = tk.Tk()
        # Create frame
        frame = Frame(root, width=300, height=300)
        frame.pack(expand=True, fill=BOTH)  # .grid(row=0,column=0)
        canvas1 = Canvas(frame, bg='#FFFFFF', width=300, height=300, scrollregion=(0, 0, 500, 500))

        # Create canvas
        # canvas1 = tk.Canvas(root, width = 400, height = 600,  relief = 'raised')
        canvas1.pack()

        # Set title for the window
        root.title("Customer Details")
        label1 = tk.Label(root, text='Customer Delivery Details')
        label1.config(font=('helvetica', 14))
        canvas1.create_window(300, 25, window=label1)

        # Customer Details Output lines
        # Type here in the 'detais'
        details = tk.Label(root, text='The Square Root of ' + ' is:', font=('helvetica', 10))
        canvas1.create_window(300, 100, window=details)

        canvas1.config(width=600, height=600)
        root.mainloop()



# Main method

prompt = Window()
# prompt.inputCustomer()
prompt.ouputWindow()
