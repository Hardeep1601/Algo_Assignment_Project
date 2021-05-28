import codecs
import os
import tkinter as tk
import webbrowser
from tkinter import *
from calcDirection import parent
from PIL import ImageTk, Image

import imgkit
from tkinter import filedialog, font
# import main as sentiment

import pdfkit as pdfkit

from tkinter_custom_button import TkinterCustomButton


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
    bestDist = 0
    bestTime = 0

    optionsHub = [
        'City-link Express',
        'Pos Laju',
        'GDEX',
        'J&T',
        'DHL'
    ]

    optionsLocation = [
        'Port Klang',
        'Petaling Jaya',
        'Batu Caves',
        'Kajang',
        'Sungai Buloh'
    ]


    # Font Format
    # font = ("Century Gothic", 11)
    # Main menu background color
    # '#e1b800'

    def mainWindow(self):
        new_window = ''

        # Insert image
        root = Tk()
        root.geometry("600x600")
        root.title('Main Window')

        # Create a photoimage object of the image in the path
        image1 = Image.open("gui_img.jpeg")
        image1 = image1.resize((600, 600), Image.ANTIALIAS)

        test = ImageTk.PhotoImage(image1)

        label1 = tk.Label(image=test)
        label1.image = test

        # Position image
        label1.place(x=0, y=0)


        lbl = Label(new_window, text='Customer Delivery App', font = ("Century Gothic", 15,'bold'), bg='#2874A6',
                    fg='#ffffff', relief="ridge", width=100, height=5, borderwidth=5)
        lbl.pack(padx=10, pady=50)


        bt = TkinterCustomButton(text='Enter new customer', corner_radius=5, command=self.inputCustomer)
        # bt.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        bt.pack(padx=10, pady=10)

        bt = TkinterCustomButton(text='Distance Details', corner_radius=5, command=self.ouputDistance)
        bt.pack(padx=10, pady=10)
        # INSERT the HTML file name for each customer
        # b = Button(root, text='Open Map', command=self.openHTML(self.customerID))
        # b.pack(padx=10, pady=10)
        bt = TkinterCustomButton(text='Start sentiment code', corner_radius=5, command=self.runSentiment)
        bt.pack(padx=10, pady=10)
        bt = TkinterCustomButton(text='Sentiment Details', corner_radius=5, command=self.outputSentiment)
        bt.pack(padx=10, pady=10)

        # Button(root, text='Close Newly Opened Window', command=lambda: new_window.destroy()).pack()





        root.mainloop()


    def inputCustomer(self):

        first = tk.Tk()
        first.title("Customer Details")
        first.config(bg='#e1b800')
        # buttonFont = font.Font(family='Century Gothic', size=11)


        # tk.Label(first, text='State the ID of customer').grid(row=0, column=1)
        tk.Label(first, text="Input details ", font=("Century Gothic", 11),bg='#2874A6',fg='#ffffff', relief="ridge", width=20, height=1, borderwidth=3 ).grid(row=1, column=1)
        # first.config(bg='#e1b800')
        # type box
        # box = tk.Entry(first)
        # box.grid(row=1, column=1)

        # tk.Label(first, text=str).grid(row=0, column=1)
        tk.Label(first, text="Origin: ",bg='#e1b800', font=("Century Gothic", 11) ).grid(row=2)
        tk.Label(first, text="Destination: ", bg='#e1b800', font=("Century Gothic", 11) ).grid(row=3)

        origin = tk.Entry(first)
        dest = tk.Entry(first)
        origin.grid(row=2, column=1)
        dest.grid(row=3, column=1)


        # STORE CUSTOMER ID AND FILE INFO

        def saveCustNum():
            # hold=box.get()
            # self.numOfCustomer = hold
            self.customerID = 1
            self.originArr.append(origin.get())
            self.destinationArr.append(dest.get())
            first.destroy()



            # Calculate the distance after pressing the submit button
            t = parent()
            t.setCustNo(self.customerID)
            t.setOrigin(self.originArr[0])
            t.setDest(self.destinationArr[0])
            print(t.getJourneyTime())
            print(t.getDistance())
            # print('t.getShort() : ', t.getShort())
            # print("Run html to image")
            self.bestDist = self.smallestVal(t.getDistance())
            self.bestTime = self.smallestVal(t.getJourneyTime())
            # print("Best distance ",self.bestDist)
            # print("Best time ",self.bestTime)
            self.saveDetails(t.getDistance(), t.getJourneyTime(), t.getShort(), t.routeDis()[0], t.routeDis()[1])



        # button widget
        b1 = Button(first, text="Submit", command=saveCustNum, bg='#2874A6', fg='#ffffff', font=("Century Gothic", 11) ).grid(row=4, column=1, sticky=E)

        first.mainloop()



    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # SENTIMENT ANALYSIS CODE #

    from prob2_1 import p2
    from threading import Thread


    def outputSentiment(self):

        first = tk.Tk()
        first.title("Sentiment Details")
        first.geometry("600x600")
        first.config(bg='#e1b800')

        # Create Label/String to be attached
        labelID = Label(first, text="\nSummary and Recommended Hub For Customer", font=("Century Gothic", 14), bg='#2874A6',
                        fg='#ffffff', relief="ridge", width=50, height=3, borderwidth=3)
        labelID.pack()
        label = Label(first, text="\nBest Distance : " + str(self.bestDist) + " km", font=("Century Gothic", 11), bg='#e1b800')
        label.pack()
        labelOrigin = Label(first, text="\nBest Journey Time : " + str(self.bestTime) + ' min', font=("Century Gothic", 11), bg='#e1b800')
        labelOrigin.pack()
        labelDestination = Label(first, text="\nBest Sentiment : "+ ' CityLink ' + ', Port Klang', font=("Century Gothic", 11), bg='#e1b800')
        labelDestination.pack()
        label2 = Label(first, text="\nRecommended Courier : " + '<route taken based on hub>', font=("Century Gothic", 11), bg='#e1b800')
        label2.pack()
        labelTime = Label(first, text="\n---------------------------\nSummary\n---------------------------\n\n"+'Sample text',
                          font=("Century Gothic", 11), bg='#e1b800')
        labelTime.pack(pady=10)


        # origin = tk.Entry(first)
        # dest = tk.Entry(first)
        # origin.grid(row=2, column=1)
        # dest.grid(row=3, column=1)



        first.mainloop()


    def runSentiment(self):
        print('Run sentiment class...')
        self.Thread(target=self.runSentimentCode).start()


    def runSentimentCode(self):
        # import p2 from prob2

        temp = self.p2()
        pos = temp.getPositive()
        neg = temp.getNegative()

        wc = temp.getWordcount()
        sw = temp.getStopwordscount()

        # Graph for wordcount and stopwords count for each courier

        wcCitylink = wc[0] + wc[1] + wc[2]
        wcPoslaju = wc[3] + wc[4] + wc[5]
        wcGdex = wc[6] + wc[7] + wc[8]
        wcJnt = wc[9] + wc[10] + wc[11]
        wcDhl = wc[12] + wc[13] + wc[14]

        swCitylink = sw[0] + sw[1] + sw[2]
        swPoslaju = sw[3] + sw[4] + sw[5]
        swGdex = sw[6] + sw[7] + sw[8]
        swJnt = sw[9] + sw[10] + sw[11]
        swDhl = sw[12] + sw[13] + sw[14]

        import plotly.graph_objects as go
        couriers = ['Citylink', 'Poslaju', 'GDEX', 'J&T', 'DHL']

        fig = go.Figure(data=[
            go.Bar(name='Word count', x=couriers, y=[wcCitylink, wcPoslaju, wcGdex, wcJnt, wcDhl]),
            go.Bar(name='Stopwords count', x=couriers, y=[swCitylink, swPoslaju, swGdex, swJnt, swDhl])
        ])
        # Change the bar mode
        fig.update_layout(barmode='group')
        fig.show()

        # Graph for positive and negative words for each courier

        totalPositiveCitylink = pos[0] + pos[1] + pos[2]
        totalPositivePoslaju = pos[3] + pos[4] + pos[5]
        totalPositiveGdex = pos[6] + pos[7] + pos[8]
        totalPositiveJnt = pos[9] + pos[10] + pos[11]
        totalPositiveDhl = pos[12] + pos[13] + pos[14]

        totalNegativeCitylink = neg[0] + neg[1] + neg[2]
        totalNegativePoslaju = neg[3] + neg[4] + neg[5]
        totalNegativeGdex = neg[6] + neg[7] + neg[8]
        totalNegativeJnt = neg[9] + neg[10] + neg[11]
        totalNegativeDhl = neg[12] + neg[13] + neg[14]

        import plotly.graph_objects as go
        couriers = ['Citylink', 'Poslaju', 'GDEX', 'Ja&T', 'DHL']

        fig = go.Figure(data=[
            go.Bar(name='Positive words', x=couriers,
                   y=[totalPositiveCitylink, totalPositivePoslaju, totalPositiveGdex, totalPositiveJnt,
                      totalPositiveDhl]),
            go.Bar(name='Negative Words', x=couriers,
                   y=[totalNegativeCitylink, totalNegativePoslaju, totalNegativeGdex, totalNegativeJnt,
                      totalNegativeDhl])
        ])
        # Change the bar mode
        fig.update_layout(barmode='group')
        fig.show()

        ct = totalPositiveCitylink - totalNegativeCitylink
        pl = totalPositivePoslaju - totalNegativePoslaju
        gd = totalPositiveGdex - totalNegativeGdex
        jn = totalPositiveJnt - totalNegativeJnt
        dh = totalPositiveDhl - totalNegativeDhl

        courierlist = [ct, pl, gd, jn, dh]

        # print(courierlist)
        def findBestSentiment():
            if ct > pl and ct > gd and ct > jn and ct > dh:
                return print('Citylink has the best sentiment')
            elif pl > ct and pl > gd and pl > jn and pl > dh:
                return print('Poslaju has the best sentiment')
            elif gd > ct and gd > pl and gd > jn and gd > dh:
                return print('GDEX has the best sentiment')
            elif jn > ct and jn > pl and jn > gd and jn > dh:
                return print('JandT has the best sentiment')
            elif dh > ct and dh > pl and dh > gd and dh > jn:
                return print('DHL has the best sentiment')

        findBestSentiment()



    # END SENTIMENT CODE #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


    def smallestVal(self, arr):
        min = arr[0]
        for i in range(len(arr)):
            if min > arr[i]:
                min = arr[i]
        return min


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
        root.geometry("600x680")
        root.title('Customer Delivery Details')
        root.config(bg='#e1b800')

        header = Label(root, text="\nCustomer Delivery Details", font=("Century Gothic", 14), bg='#2874A6',
                        fg='#ffffff', relief="ridge", width=50, height=3, borderwidth=3)
        header.pack(pady=10)


        # Create Label/String to be attached
        # labelID = Label(root, text="\nCustomer ID: "+ self.customerID)
        # labelID.pack()
        label = Label(root, text="\nCalculate distance between 2 points", font=("Century Gothic", 11), bg='#e1b800')
        label.pack()
        labelOrigin = Label(root, text="\nOrigin : " + self.originArr[0], font=("Century Gothic", 11), bg='#e1b800')
        labelOrigin.pack()
        labelDestination = Label(root, text="\nDestination : " + self.destinationArr[0], font=("Century Gothic", 11), bg='#e1b800')
        labelDestination.pack()
        label2 = Label(root, text="\nDistance between 2 points : " + str(self.distance2point), font=("Century Gothic", 11), bg='#e1b800')
        label2.pack()
        labelTime = Label(root, text="\nTime taken : " + str(self.time2point), font=("Century Gothic", 11), bg='#e1b800')
        labelTime.pack()

        # CREATE HUB DROPDOWN
        label3 = Label(root, text="\n\nSelect Hub", bg='#e1b800', font=("Century Gothic", 12))
        label3.pack()
        # Change the label text

        # Dropdown menu options


        # initial menu text
        # clicked1.set('Select a hub')
        def showHub(*args):
            getIndex = self.optionsHub.index(clicked1.get())
            labelHub1.config(text="\nHub Name : " + str(self.optionsHub[getIndex]))
            labelHub2.config(text="\nHub Location : " + str(self.optionsLocation[getIndex]))
            labelHub.config(text="\nDistance between 3 points : " + str(self.distanceArr[getIndex]) + ' km')
            labelTime2.config(text="\nTime taken : " + str(self.timeArr[getIndex]) + ' min')

        clicked1 = StringVar(value="Select a hub")
        clicked1.trace("w", showHub)

        # Create Dropdown menu
        drop1 = OptionMenu(root, clicked1, *self.optionsHub)
        drop1.pack()
        labelHub1 = Label(root, text="\nHub Name :\t--", font=("Century Gothic", 11), bg='#e1b800')
        labelHub1.pack()
        labelHub2 = Label(root, text="\nHub Location :\t--", font=("Century Gothic", 11), bg='#e1b800')
        labelHub2.pack()
        labelHub = Label(root, text="\nDistance between 3 points :\t--", font=("Century Gothic", 11), bg='#e1b800')
        labelHub.pack()
        labelTime2 = Label(root, text="\nTime taken :\t--", font=("Century Gothic", 11), bg='#e1b800')
        labelTime2.pack()
        labelFastest = Label(root, text="\nFastest Hub : " + self.optionsHub[self.shortestIndex], font=("Century Gothic", 11), bg='#e1b800')
        labelFastest.pack()

        # INSERT the HTML file name for each customer
        b = Button(root, text='Open Map', command=self.openHTML(self.customerID), font=("Century Gothic", 11), bg='#e1b800')
        # b.pack(pady=5)

        # Execute tkinter
        root.mainloop()

    import codecs
    import threading
    import time

    def openHTML(self, num):
        # nameStr = 'C:\Users\harde\Documents\Algo Assignment Project\\' +fileName
        # self.Thread(target=(webbrowser.open_new_tab(r'C:\Users\harde\Documents\Algo Assignment Project\cus1.html'))).start()

        # self.threading.Thread(target=(webbrowser.open_new_tab(r'C:\Users\harde\Documents\Algo Assignment Project\cus1.html'))).start()
        return os.startfile(r'C:\Users\harde\Documents\Algo Assignment Project\cus1.html')
        # return os.startfile(r'C:\Users\harde\Documents\Algo Assignment Project\map.html')






# Main method of PROBLEM 1

# prompt = Window()
# prompt.inputCustomer()

# Call distance mapping algorithm to get distance and map
# <---HERE--->
# a = [12, 13, 14]
# prompt.ouputWindow(a)
