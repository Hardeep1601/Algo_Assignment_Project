import os
import tkinter as tk
from tkinter import *
from tkinter import filedialog


class Window:

    numOfCustomer = 0
    originArr = []
    destinationArr = []
    htmlFile = []

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
    def ouputWindow(self, distanceArr):
        root = tk.Tk()

        # Adjust size
        root.geometry("800x600")

        # Create a dropdown menu
        # ----------------------------------------

        # Dropdown menu options
        # Change the label text
        def show():
            labelS.config(text=clicked.get())

        options = []
        for i in range(5):
            options.append('Customer ' + str(i + 1))
        # datatype of menu text
        clicked = StringVar()

        # initial menu text
        clicked.set(options[0])

        # Create Dropdown menu
        drop = OptionMenu(root, clicked, *options)
        drop.pack()

        # Create button, it will change label text
        button = Button(root, text="Update Page", command=show).pack()

        # Create Label/String to be attached
        labelS = Label(root, text="\nHello")
        labelS.pack()

        # end Dropdown

        # Create frame
        # frame = Frame(root, width=300, height=300)
        # frame.pack(expand=True, fill=BOTH)  # .grid(row=0,column=0)
        canvas1 = Canvas(drop, bg='#FFFFFF', width=300, height=300, scrollregion=(0, 0, 3000, 3000))

        # Create canvas
        canvas1 = tk.Canvas(root, width = 400, height = 600,  relief = 'raised')
        canvas1.pack()

        # Set title for the window
        root.title("Customer Details")
        label1 = tk.Label(root,
                          text='Customer Delivery Details\n---------------------------------------------------------------')
        label1.config(font=('helvetica', 14))
        # canvas1.create_window(300, 25, window=label1)
        # End root window declaration

        # Customer Details Output lines
        for i in range(int(self.numOfCustomer)):
            bHeight = 80 + (i * 80)
            custStr = 'Customer %d' % (i+1)

            # Customer number
            custLabel = tk.Label(root, text=(custStr+' : '))
            custLabel.config(font=('helvetica', 12))
            canvas1.create_window(100, bHeight, window=custLabel)

            # Show DISTANCE for each customer
            # strDistance = '20.00 km'
            distLabel = tk.Label(root, text=distanceArr[i])
            distLabel.config(font=('helvetica', 12))
            # canvas1.create_window(200, bHeight, window=distLabel)


            # Show origin to destination POINTS
            # Get the Origin and destination
            pointsStr = '%s  ---->  %s' % (self.originArr[i], self.destinationArr[i])
            pointsLabel = tk.Label(root, text=pointsStr)
            pointsLabel.config(font=('helvetica', 12))
            # canvas1.create_window(200, bHeight+40, window=pointsLabel)



            # BUTTON to open file
            # INSERT the HTML file name for each customer
            b = Button(root, text=custStr + ' Map', command=self.openHTML(i))
            # canvas1.create_window(500, bHeight, window=b)


        root.mainloop()

    def saveFileName(self, fileName):
        for i in range(len(fileName)):
            nameStr = r'C:\Users\harde\Documents\Algo Assignment Project\\' + fileName[i]
            self.htmlFile.append(nameStr)

    def openHTML(self, num):
        # nameStr = 'C:\Users\harde\Documents\Algo Assignment Project\\' +fileName
        return os.startfile(self.htmlFile[num])
        # return os.startfile(r'C:\Users\harde\Documents\Algo Assignment Project\map.html')





# Main method of PROBLEM 1

prompt = Window()
# prompt.inputCustomer()

# Call distance mapping algorithm to get distance and map
# <---HERE--->
a = [12, 13, 14]
prompt.ouputWindow(a)
