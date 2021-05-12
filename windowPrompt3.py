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
    def ouputWindow(self, distanceArr, timeArr, shortestTimeArr):
        root = tk.Tk()

        # Adjust size
        root.geometry("800x600")
        root.title('Customer Delivery Details')

        # Change the label text
        def show(*args):
            getIndex = options.index(clicked.get())
            shortestIndex = shortestTimeArr[int(getIndex)]
            print('Test ;', shortestIndex)
            shortestHold = shortestIndex + getIndex*5
            labelOrigin.config(text="\nOrigin : " + self.originArr[getIndex])
            labelDestination.config(text="\nDestination :\t" + self.destinationArr[getIndex])
            labelTime.config(text="\nTime taken :\t" + timeArr[shortestHold])
            label2.config(text="\nDistance between 2 points :\t" + distanceArr[shortestHold])


        # Dropdown menu options
        options = []
        for i in range(5):
            options.append('Customer ' + str(i + 1))

        optionsFee = []
        for i in range(5):
            optionsFee.append('Customer Fee ' + str(i + 1))

        header = Label(root, text="Customer Delivery Details\n\nSelect Customer Number")
        header.config(font=('Times', 14))
        header.pack()

        # Create Dropdown menu
        clicked = StringVar(value="Select a hub")
        clicked.trace("w", show)
        drop = OptionMenu(root, clicked, *options)
        drop.pack()

        # Create Label/String to be attached
        label = Label(root, text="\nCalculate distance between 2 points")
        label.pack()
        labelOrigin = Label(root, text="\nOrigin : ")
        labelOrigin.pack()
        labelDestination = Label(root, text="\nDestination : ")
        labelDestination.pack()
        label2 = Label(root, text="\nDistance between 2 points :\t--")
        label2.pack()
        labelTime = Label(root, text="\nTime taken :\t--")
        labelTime.pack()

        # CREATE HUB DROPDOWN
        label3 = Label(root, text="\n\nSELCECT CUSTOMER HUB")
        label3.pack()
        # Change the label text

        # Dropdown menu options
        optionsHub = [
            'City-link Express',
            'Pos Laju',
            'GDEX',
            'J&T',
            'DHL'
        ]

        # initial menu text
        # clicked1.set('Select a hub')
        def showHub(*args):
            getIndex = optionsHub.index(clicked1.get())
            labelHub.config(text="\nDistance between 3 points :\t" + optionsHub[getIndex])
            labelTime2.config(text="\nTime taken :\t")

        clicked1 = StringVar(value="Select a hub")
        clicked1.trace("w", showHub)

        # Create Dropdown menu
        drop1 = OptionMenu(root, clicked1, *optionsHub)
        drop1.pack()
        labelHub = Label(root, text="\nDistance between 3 points :\t--")
        labelHub.pack()
        labelTime2 = Label(root, text="\nTime taken :\t--")
        labelTime2.pack()

        # Execute tkinter
        root.mainloop()
        # End Window Create and Config
        # ---------------------------------------------------
        #

        # Customer Details Output lines
        for i in range(int(self.numOfCustomer)):
            bHeight = 80 + (i * 80)
            custStr = 'Customer %d' % (i+1)

            # Customer number
            custLabel = tk.Label(root, text=(custStr+' : '))
            custLabel.config(font=('helvetica', 12))
            # canvas1.create_window(100, bHeight, window=custLabel)

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

# prompt = Window()
# prompt.inputCustomer()

# Call distance mapping algorithm to get distance and map
# <---HERE--->
# a = [12, 13, 14]
# prompt.ouputWindow(a)
