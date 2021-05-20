from calcDirection import parent
from windowPrompt3 import Window

# Declaring the main class
w = Window()
w.inputCustomer()

distArr = []
shortestArr = []
fileArr = []

print(w.originArr)
print(w.destinationArr)

t = parent()



# Used to calculate distance between 2 points
for i in range(int(w.numOfCustomer)):
    t.setCustNo(w.customerID)
    t.setOrigin(w.originArr[i])
    t.setDest(w.destinationArr[i])
    hold = t.getShort()
    print('Hold : ', hold)
    index = hold+(i*5)
    # index = hold
    # holdTime = timeArr[]

    fileArr.append(t.getDirectory())
    print(t.getJourneyTime())
    print(t.getDistance())
    # t.clearArr()
    print('t.getShort() : ', t.getShort())
    # w.htmlToImage()
    print("Run html to image")
    # print('Route distance: ', t.routeDis()[1])
    w.ouputWindow(t.getDistance(), t.getJourneyTime(), t.getShort(), t.routeDis()[0], t.routeDis()[1])
    print('test')
    # Both the distance array are the same for 2 different points
    # print(distArr)
    # print(shortestArr)

# Output window
# Problem: only got one customer HTML file cuz of only 1 directory
# Problem 2: File open straight away after window launches
w.saveFileName(fileArr)


# print(distArr)
# print(shortestArr)
# # Set Origin
# t.setOrigin('Bukit Jelutong')
# # Set Destination
# t.setDest('Ampang Jaya')
# # returns all journey time
# print(t.getJourneyTime())
# # returns all distances
# print(t.getDistance())
# # return the index of shortest time (used to get shortest path from JourneyTime and Distance list)
# print(t.getShort())
# # returns the file location
# print(t.getDirectory())


# a=[2,3,4,5,2]
#
# print(a.index(2))