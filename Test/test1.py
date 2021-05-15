import pdfkit

from calcDirection import parent
from windowPrompt3 import Window

# Declaring the main class
w = Window()
# w.inputCustomer()


import imgkit

path_wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
# config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)
config = pdfkit.configuration(wkhtmltopdf=bytes(path_wkhtmltopdf, 'utf-8'))

# fileName = 'cusTest' + str(self.customerID) + '.jpg'
# print(fileName)/
imgkit.from_file(r'C:\Users\harde\Documents\Algo Assignment Project\cus1.html', 'cusTest.jpg', config=config)

# Used to calculate distance between 2 points
for i in range(1):
    # t.setCustNo(1)
    # t.setOrigin(w.originArr[i])
    # t.setDest(w.destinationArr[i])
    # hold = t.getShort()
    # print('Hold : ', hold)
    # index = hold+(i*5)
    # index = hold
    # holdTime = timeArr[]


    # w.htmlToImage()
    print("Run html to image")
    # w.ouputWindow(t.getDistance(), t.getJourneyTime(), t.getShort())

# Output window
# Problem: only got one customer HTML file cuz of only 1 directory
# Problem 2: File open straight away after window launches
# w.saveFileName(fileArr)