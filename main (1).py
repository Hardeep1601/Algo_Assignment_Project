from calcDirection import parent
from windowPrompt3 import Window

# Declaring the main class
w = Window()
w.inputCustomer()

distArr = []
shortestArr = []
fileArr = []

# print(w.originArr)
# print(w.destinationArr)

t = parent()



# Used to calculate distance between 2 points
for i in range(int(w.numOfCustomer)):
    t.setCustNo(w.customerID)
    t.setOrigin(w.originArr[i])
    t.setDest(w.destinationArr[i])
    # hold = t.getShort()
    # print('Hold : ', hold)
    # index = hold+(i*5)


    fileArr.append(t.getDirectory())
    print(t.getJourneyTime())
    print(t.getDistance())
    print('t.getShort() : ', t.getShort())
    print("Run html to image")
    w.saveDetails(t.getDistance(), t.getJourneyTime(), t.getShort(), t.routeDis()[0], t.routeDis()[1])
    w.mainWindow()
    # w.ouputWindow()
    # print('test')



# w.saveFileName(fileArr)

