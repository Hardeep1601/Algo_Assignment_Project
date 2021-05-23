import os
import tkinter as tk
from tkinter import *
from calcDirection import parent
import imgkit
from tkinter import filedialog


import pdfkit as pdfkit


class Window:

    numOfCustomer = 1
    originArr = []
    destinationArr = []
    htmlFile = []
    customerID = 0

    shortestIndex = 0
    # For hubs
    timeArr = []
    distanceArr = []
    # For door to door
    distance2point = 0
    time2point = 0







    def mainWindow(self):
        new_window = ''

        def openMain():
            # global new_window
            new_window = Toplevel(root)
            new_window.geometry("250x250")
            new_window.title("New Window")
            new_window.resizable(False, False)
            lbl = Label(new_window, text='I am a new window')
            lbl.pack()
            btn2 = Button(new_window, text='Close Me', command=lambda: new_window.destroy())
            btn2.pack()

        root = Tk()
        lbl = Label(new_window, text='Customer Delivery App')
        lbl.pack()
        bt = Button(root, text='Enter new customer', command=self.inputCustomer)
        bt.pack(padx=10, pady=10)
        bt = Button(root, text='Distance Details', command=self.ouputDistance)
        bt.pack(padx=10, pady=10)
        bt = Button(root, text='Sentiment Details', command=openMain)
        bt.pack(padx=10, pady=10)

        Button(root, text='Close Newly Opened Window', command=lambda: new_window.destroy()).pack()

        root.geometry("500x500")
        root.title('Main Window')
        root.mainloop()


    def inputCustomer(self):

        first = tk.Tk()
        first.title("Customer Details")
        # tk.Label(first, text='State the ID of customer').grid(row=0, column=1)
        tk.Label(first, text="Customer ID: ").grid(row=1)

        # type box
        box = tk.Entry(first)
        box.grid(row=1, column=1)

        # tk.Label(first, text=str).grid(row=0, column=1)
        tk.Label(first, text="Origin: ").grid(row=2)
        tk.Label(first, text="Destination: ").grid(row=3)

        origin = tk.Entry(first)
        dest = tk.Entry(first)
        origin.grid(row=2, column=1)
        dest.grid(row=3, column=1)


        # STORE CUSTOMER ID AND FILE INFO

        def saveCustNum():
            hold=box.get()
            # self.numOfCustomer = hold
            self.customerID = hold
            self.originArr.append(origin.get())
            self.destinationArr.append(dest.get())
            first.destroy()

            ###################
            # Clear all the array so that the correct values will be displayed






            # Calculate the distance after pressing the submit button
            t = parent()
            t.setCustNo(self.customerID)
            t.setOrigin(self.originArr[0])
            t.setDest(self.destinationArr[0])
            print(t.getJourneyTime())
            print(t.getDistance())
            print('t.getShort() : ', t.getShort())
            print("Run html to image")
            self.saveDetails(t.getDistance(), t.getJourneyTime(), t.getShort(), t.routeDis()[0], t.routeDis()[1])



        # button widget
        b1 = Button(first, text="Submit", command=saveCustNum).grid(row=4, column=1, sticky=E)

        first.mainloop()







    def saveDetails(self, distanceArr, timeArr, shortestIndex, distance2point, time2point):
        self.shortestIndex = shortestIndex
        self.distance2point = distance2point
        self.time2point = time2point
        self.timeArr = timeArr
        self.distanceArr = distanceArr





    # Create output window for program
    def ouputDistance(self):
        root = tk.Tk()

        # Adjust size
        root.geometry("800x600")
        root.title('Customer Delivery Details')



        header = Label(root, text="Customer Delivery Details\n")
        header.config(font=('Times', 14))
        header.pack()


        # Create Label/String to be attached
        labelID = Label(root, text="\nCustomer ID: "+ self.customerID)
        labelID.pack()
        label = Label(root, text="\nCalculate distance between 2 points")
        label.pack()
        labelOrigin = Label(root, text="\nOrigin : " + self.originArr[0])
        labelOrigin.pack()
        labelDestination = Label(root, text="\nDestination : " + self.destinationArr[0])
        labelDestination.pack()
        label2 = Label(root, text="\nDistance between 2 points : " + str(self.distance2point))
        label2.pack()
        labelTime = Label(root, text="\nTime taken : " + str(self.time2point))
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
            labelHub.config(text="\nDistance between 3 points : " + str(self.distanceArr[getIndex]) + ' km')
            labelTime2.config(text="\nTime taken : " + str(self.timeArr[getIndex]) + ' min')

        clicked1 = StringVar(value="Select a hub")
        clicked1.trace("w", showHub)

        # Create Dropdown menu
        drop1 = OptionMenu(root, clicked1, *optionsHub)
        drop1.pack()
        labelHub = Label(root, text="\nDistance between 3 points :\t--")
        labelHub.pack()
        labelTime2 = Label(root, text="\nTime taken :\t--")
        labelTime2.pack()
        labelFastest = Label(root, text="\nFastest Hub : " + optionsHub[self.shortestIndex])
        labelFastest.pack()

        # INSERT the HTML file name for each customer
        b = Button(root, text='Open Map', command=self.openHTML(self.customerID))

        # Execute tkinter
        root.mainloop()



    def openHTML(self, num):
        # nameStr = 'C:\Users\harde\Documents\Algo Assignment Project\\' +fileName
        return os.startfile('cus'+str(num)+'.html')
        # return os.startfile(r'C:\Users\harde\Documents\Algo Assignment Project\map.html')





# Main method of PROBLEM 1

# prompt = Window()
# prompt.inputCustomer()

# Call distance mapping algorithm to get distance and map
# <---HERE--->
# a = [12, 13, 14]
# prompt.ouputWindow(a)
