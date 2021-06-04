import codecs
import os
import tkinter as tk
import webbrowser
from tkinter import *

# import Prob_3
from Prob_3 import sentiment
from calcDirection import parent
from PIL import ImageTk, Image
import plotly.graph_objects as go

# import imgkit
from tkinter import filedialog, font
# import main as sentiment

# import pdfkit as pdfkit

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
    oritimeArr = []
    distanceArr = []
    oridistanceArr = []
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
        tk.Label(first, text="Input details ", font=("Century Gothic", 11),bg='#2874A6',fg='#ffffff', relief="ridge",
                 width=20, height=1, borderwidth=3 ).grid(row=1, column=1)
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

            self.originArr.clear()
            self.destinationArr.clear()
            self.timeArr.clear()
            self.distanceArr.clear()
            self.oritimeArr.clear()
            self.oridistanceArr.clear()

            self.originArr.append(origin.get())
            self.destinationArr.append(dest.get())
            first.destroy()



            # Calculate the distance after pressing the submit button
            self.t = parent()
            # self.t.se
            self.t.setCustNo(self.customerID)
            self.t.setOrigin(self.originArr[0])
            self.t.setDest(self.destinationArr[0])
            print(self.t.getJourneyTime())
            print(self.t.getDistance())
            # print('t.getShort() : ', t.getShort())
            # print("Run html to image")
            self.bestDist = self.smallestVal(self.t.getDistance())
            self.bestTime = self.smallestVal(self.t.getJourneyTime())
            # print("Best distance ",self.bestDist)
            # print("Best time ",self.bestTime)
            self.saveDetails(self.t.getDistance(), self.t.getJourneyTime(), self.t.getShort(), self.t.routeDis()[0], self.t.routeDis()[1])



        # button widget
        b1 = Button(first, text="Submit", command=saveCustNum, bg='#2874A6', fg='#ffffff', font=("Century Gothic", 11) ).grid(row=4, column=1, sticky=E)

        first.mainloop()



    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # SENTIMENT ANALYSIS CODE #

    from prob2_1 import p2
    from threading import Thread

    # Array = [positive_words, negative_words]
    totalCityLink = []
    totalPoslaju = []
    totalGdex = []
    totalJnt = []
    totalDhl = []

    def outputSentiment(self):

        # Problem 3 Methods
        ##############################

        p = sentiment()

        cour = ['City-link Express', 'Pos Laju', 'GDEX', 'J&T', 'DHL']

        # t=parent()
        # time = t.getJourneyTime()
        # timeC = t.courier_name.copy()
        # time = [77, 49, 67, 98, 50]
        time = self.timeArr
        timeC = cour.copy()
        # dis = [74.1, 37.2, 55.6, 95.3, 37.3]
        dis = self.distanceArr
        disC = cour.copy()
        # dis = t.getDistance().copy()
        # disC = t.courier_name.copy()

        # sent=p2()
        # pos=sent.positive
        # pos = [69, 105, 299, 48, 57, 64, 167, 17, 46, 30, 163, 43, 87, 219, 97]
        # pos = [(pos[0] + pos[1] + pos[2]), (pos[3] + pos[4] + pos[5]), (pos[6] + pos[7] + pos[8]),
        #        (pos[9] + pos[10] + pos[11]), (pos[12] + pos[13] + pos[14])]
        pos = [self.totalCityLink[0], self.totalPoslaju[0], self.totalGdex[0], self.totalJnt[0], self.totalDhl[0]]
        posC = cour.copy()

        # neg=sent.negative
        # neg = [29, 70, 232, 26, 32, 33, 93, 1, 15, 32, 44, 51, 96, 152, 32]
        # neg = [(neg[0] + neg[1] + neg[2]), (neg[3] + neg[4] + neg[5]), (neg[6] + neg[7] + neg[8]),
        #        (neg[9] + neg[10] + neg[11]), (neg[12] + neg[13] + neg[14])]
        neg = [self.totalCityLink[1], self.totalPoslaju[1], self.totalGdex[1], self.totalJnt[1], self.totalDhl[1]]
        negC = cour.copy()

        # Sentiment Probability
        # sentProb = [(pos[0] / (pos[0] + neg[0])), (pos[1] / (pos[1] + neg[1])), (pos[2] / (pos[2] + neg[2])),
        #             (pos[3] / (pos[3] + neg[3])), (pos[4] / (pos[4] + neg[4]))]

        sentProb = [
            (self.totalCityLink[0]) / (self.totalCityLink[0]+self.totalCityLink[1]),
            (self.totalPoslaju[0]) / (self.totalPoslaju[0] + self.totalPoslaju[1]),
            (self.totalGdex[0]) / (self.totalGdex[0] + self.totalGdex[1]),
            (self.totalJnt[0]) / (self.totalJnt[0] + self.totalJnt[1]),
            (self.totalDhl[0]) / (self.totalDhl[0] + self.totalDhl[1]),
        ]
        courProb = cour.copy()

        # Final courier and probability
        finCou = ['City-link Express', 'Pos Laju', 'GDEX', 'J&T', 'DHL']
        finProb = p.calcProb(sentProb, finCou, time)

        # toString methods
        sTime = p.timeString(timeC, time)
        # self.optionsHub = disC
        sDis = p.disString(disC, dis)
        sPos = p.sentString(posC, pos)
        sNeg = p.sentString(negC, neg)
        sSent = p.sentString(courProb, sentProb)
        sFin = p.sentString(finCou, finProb)

        # print(pos)
        # print(neg)
        print('The Fastest Courier =', sTime)
        print('The Shortest Route', sDis)
        print('The courier with positive review: ', sPos)
        print('The courier with negative review: ', sNeg)
        print(sSent)
        print(sFin)

        ##############################
        # Run 1
        # The Fastest Courier = Pos Laju ( 49 Minutes ) --> DHL ( 50 Minutes ) --> GDEX ( 1Hour 7 Minutes ) --> City-link Express ( 1Hour 17 Minutes ) --> J&T ( 1Hour 38 Minutes )
        # The Shortest Route Pos Laju ( 37.2 KM ) --> DHL ( 37.3 KM ) --> GDEX ( 55.6 KM ) --> City-link Express ( 74.1 KM ) --> J&T ( 95.3 KM )
        # The courier with positive review:  City-link Express ( 473.0000 ) --> DHL ( 403.0000 ) --> J&T ( 236.0000 ) --> GDEX ( 230.0000 ) --> Pos Laju ( 169.0000 )
        # The courier with negative review:  City-link Express ( 331.0000 ) --> DHL ( 280.0000 ) --> J&T ( 127.0000 ) --> GDEX ( 109.0000 ) --> Pos Laju ( 91.0000 )
        # GDEX ( 0.6785 ) --> J&T ( 0.6501 ) --> Pos Laju ( 0.6500 ) --> DHL ( 0.5900 ) --> City-link Express ( 0.5883 )
        # Pos Laju ( 0.5566 ) --> GDEX ( 0.5452 ) --> DHL ( 0.5035 ) --> J&T ( 0.4633 ) --> City-link Express ( 0.4555 )


        # Run 2



        first = tk.Tk()
        first.title("Sentiment Details")
        first.geometry("1200x600")
        first.config(bg='#e1b800')

        # Create Label/String to be attached
        labelID = Label(first, text="\nSummary and Recommended Hub For Customer", font=("Century Gothic", 14), bg='#2874A6',
                        fg='#ffffff', relief="ridge", width=50, height=3, borderwidth=3)
        labelID.pack()
        # label = Label(first, text="\nBest Distance : " + str(self.bestDist[0]) + " km, "+str(cour[self.bestDist[1]]), font=("Century Gothic", 11), bg='#e1b800')
        # label.pack()
        # labelOrigin = Label(first, text="\nBest Journey Time : " + str(self.bestTime[0]) + ' min, '+str(cour[self.bestTime[1]]), font=("Century Gothic", 11), bg='#e1b800')
        # labelOrigin.pack()

        label = Label(first, text='\n\nThe Fastest Courier: '+ sTime+
                                  '\n\nThe Shortest Route: '+ sDis+
                                  '\n\nThe courier with positive review: '+ sPos+
                                  '\n\nThe courier with negative review: '+ sNeg+
                                  '\n\nThe probability distribution of routes : ' + sSent +
                                  '\n\nThe recommended courier for customer: '+ sFin,
                      font=("Century Gothic", 11), bg='#e1b800')
        label.pack()
        # Route Probability



        # labelDestination = Label(first, text="\nBest Sentiment : "+ ' CityLink ' + ', Port Klang', font=("Century Gothic", 11), bg='#e1b800')
        # labelDestination.pack()


        # label2 = Label(first, text="\nRecommended Courier : " + '<route taken based on hub>', font=("Century Gothic", 11), bg='#e1b800')
        # label2.pack()



        # Summary
        summaryStr = 'The courier with the best distance is '+ str(cour[self.bestDist[1]]) +'. The courier with the best journey time is '+ str(cour[self.bestTime[1]]) +\
                     '\nThe courier with the best sentiment is CityLink. Based on all the data obtained, the recommended courier is decided based on 3 aspects, \n' \
                     'fastest courier, shortest courier and best sentiment analysis ration. Thus, the recommended courier for this customer is sorted in acending \n ' \
                     'order, from the preffered choice to the least preferred choice.'

        labelTime = Label(first, text="\n---------------------------\nSummary\n---------------------------\n\n"+'Sample text\n'+summaryStr,
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


        # Parse values into array
        self.totalCityLink = [totalPositiveCitylink, totalNegativeCitylink]
        self.totalPoslaju = [totalPositivePoslaju, totalNegativePoslaju]
        self.totalGdex = [totalPositiveGdex, totalNegativeGdex]
        self.totalJnt = [totalPositiveJnt, totalNegativeJnt]
        self.totalDhl = [totalPositiveDhl, totalNegativeDhl]



        # import plotly.graph_objects as go
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
        index = 0
        for i in range(len(arr)):
            if min > arr[i]:
                min = arr[i]
                index = i
        return min,index


    def saveDetails(self, distanceArr, timeArr, shortestIndex, distance2point, time2point):
        self.shortestIndex = shortestIndex
        self.distance2point = distance2point
        self.time2point = time2point
        self.timeArr = timeArr
        self.distanceArr = distanceArr
        self.oridistanceArr = distanceArr
        self.oritimeArr = timeArr








    # Create output window for program
    def ouputDistance(self):
        root = tk.Tk()

        # # Adjust size
        root.geometry("600x680")

        root.title('Customer Delivery Details')
        root.config(bg='#e1b800')
        b = Button(root, text="All Map",command=lambda :self.openHTML(2), font=("Century Gothic", 11), bg='#2874A6',
                    fg='#ffffff')
        b.place(relx=0.3,rely=0.9)
        b = Button(root, text="Hub Map",command=lambda :self.openHTML(1), font=("Century Gothic", 11), bg='#2874A6',
                    fg='#ffffff',  )
        b.place(relx=0.6, rely=0.9)

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
        labelFastest = Label(root, text="\nFastest Hub : " + self.optionsHub[self.shortestIndex],
                             font=("Century Gothic", 11, 'italic'), bg='#e1b800')
        labelFastest.pack()
        # Change the label text

        # Dropdown menu options
        # initial menu text
        # clicked1.set('Select a hub')
        def showHub(*args):
            getIndex = self.optionsHub.index(variable.get())
            self.t.setHub(str(self.optionsHub[getIndex]))
            labelHub1.config(text="\nHub Name : " + str(self.optionsHub[getIndex]))
            labelHub2.config(text="\nHub Location : " + str(self.optionsLocation[getIndex]))
            labelHub.config(text="\nDistance between 3 points : " + str(self.oridistanceArr[getIndex]) + ' km')
            labelTime2.config(text="\nTime taken : " + str(self.oritimeArr[getIndex]) + ' min')

        # master = Tk()
        variable = StringVar(root)
        variable.set('DHL')
        variable.trace("w", showHub)

        # Create Dropdown menu
        drop1 = OptionMenu(root, variable, *self.optionsHub)
        drop1.pack()
        s=self.shortestIndex
        labelHub1 = Label(root, text="\nHub Name :\t"+str(self.optionsHub[s]), font=("Century Gothic", 11), bg='#e1b800')
        labelHub1.pack()
        labelHub2 = Label(root, text="\nHub Location :\t"+str(self.optionsLocation[s]) , font=("Century Gothic", 11), bg='#e1b800')
        labelHub2.pack()
        labelHub = Label(root, text="\nDistance between 3 points :\t"+str(self.oridistanceArr[s]) + ' km', font=("Century Gothic", 11), bg='#e1b800')
        labelHub.pack()
        labelTime2 = Label(root, text="\nTime taken :\t"+ str(self.oritimeArr[s]) + ' min', font=("Century Gothic", 11), bg='#e1b800')
        labelTime2.pack()


        # Execute tkinter
        root.mainloop()

    import codecs
    import threading
    import time

    def openHTML(self, num):
        # nameStr = 'C:\Users\harde\Documents\Algo Assignment Project\\' +fileName
        # self.Thread(target=(webbrowser.open_new_tab(r'C:\Users\harde\Documents\Algo Assignment Project\cus1.html'))).start()
        # self.threading.Thread(target=(webbrowser.open_new_tab(r'C:\Users\harde\Documents\Algo Assignment Project\cus1.html'))).start()
        if num==1:
            return os.startfile(r'cus1.html')
        else:
            return os.startfile(r'cus1all.html')
        # return os.startfile(r'C:\Users\harde\Documents\Algo Assignment Project\map.html')






# Main method of PROBLEM 1

# prompt = Window()
# prompt.inputCustomer()

# Call distance mapping algorithm to get distance and map
# <---HERE--->
# a = [12, 13, 14]
# prompt.ouputWindow(a)
