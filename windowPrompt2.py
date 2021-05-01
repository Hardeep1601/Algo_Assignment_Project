import os
import tkinter as tk
from tkinter import *
from tkinter import filedialog


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
        canvas1 = Canvas(frame, bg='#FFFFFF', width=300, height=300, scrollregion=(0, 0, 3000, 3000))

        # Create canvas
        # canvas1 = tk.Canvas(root, width = 400, height = 600,  relief = 'raised')
        canvas1.pack()

        # Set title for the window
        root.title("Customer Details")
        label1 = tk.Label(root, text='Customer Delivery Details\n---------------------------------------------------------------')
        label1.config(font=('helvetica', 14))
        canvas1.create_window(300, 25, window=label1)

        # Customer Details Output lines
        for i in range(int(self.numOfCustomer)):
            bHeight = 80 + (i * 80)
            custStr = 'Customer %d' % (i+1)

            # Customer number
            custLabel = tk.Label(root, text=(custStr+' : '))
            custLabel.config(font=('helvetica', 12))
            canvas1.create_window(100, bHeight, window=custLabel)

            # Show DISTANCE for each customer
            strDistance = '20.00 km'
            distLabel = tk.Label(root, text=strDistance)
            distLabel.config(font=('helvetica', 12))
            canvas1.create_window(200, bHeight, window=distLabel)


            # Show origin tp destination POINTS
            # Get the Origin and destination
            pointsStr = '%s  ---->  %s' % (self.originArr[i], self.destinationArr[i])
            pointsLabel = tk.Label(root, text=pointsStr)
            pointsLabel.config(font=('helvetica', 12))
            canvas1.create_window(200, bHeight+40, window=pointsLabel)



            # BUTTON to open file
            # INSERT the HTML file name for each customer
            b = Button(root, text=custStr + ' Map', command=self.openHTML)
            canvas1.create_window(500, bHeight, window=b)


        # Vertical bar
        vbar=Scrollbar(frame,orient=VERTICAL)
        vbar.pack(side=RIGHT,fill=Y)
        vbar.config(command=canvas1.yview)

        canvas1.config(width=600, height=600)
        canvas1.config(yscrollcommand=vbar.set)
        canvas1.pack(side=LEFT,expand=True,fill=BOTH)
        root.mainloop()

    def openHTML(self):
        # file = filedialog.askopenfilename(initialdir="/map.html")
        # label = Label(root, text=file).pack()
        # htmlFile =
        return os.startfile(r'C:\Users\harde\Documents\Algo Assignment Project\map.html')


# Main method of PROBLEM 1

prompt = Window()
prompt.inputCustomer()

# Call distance mapping algorithm to get distance and map
# <---HERE--->

prompt.ouputWindow()
