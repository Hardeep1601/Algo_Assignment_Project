from calcDirection import parent
from prob2_1 import p2


def insertionSort(arr,aby):
    for i in range(1, len(arr)):

        key = arr[i]
        key1=aby[i]
        j = i-1
        while j >= 0 and key < arr[j] :
                arr[j + 1] = arr[j]
                aby[j + 1] = aby[j]

                j -= 1
        arr[j + 1] = key
        aby[j + 1] = key1

def insertionSortRev(arr,aby):
    for i in range(1, len(arr)):

        key = arr[i]
        key1=aby[i]
        j = i-1
        while j >= 0 and key > arr[j] :
                arr[j + 1] = arr[j]
                aby[j + 1] = aby[j]

                j -= 1
        arr[j + 1] = key
        aby[j + 1] = key1


def timeString(cour,arr):
    # initialize an empty string
    insertionSort(arr,cour)
    temp = ""

    # traverse in the string
    for i in range (len(cour)):
        temp += cour[i]
        # temp+= arr[i].__str__()
        if(arr[i]>=60):
            z=arr[i]/60
            z=int(z)
            y=(arr[i]-z*60)
            temp += ' ( '+str(z)+'Hour '+str(y)+' Minutes )'
        else:
            temp += ' ( ' + str(arr[i]) + ' Minutes )'

        if i!= 4:
            temp+= ' --> '
        # return string
    return temp

def disString(cour,arr):
    # initialize an empty string
    temp = ""
    insertionSort(arr,cour)
    # traverse in the string
    for i in range (len(cour)):
        temp += cour[i]
        # temp+= arr[i].__str__()

        temp += ' ( '+str(arr[i])+' KM )'


        if i!= 4:
            temp+= ' --> '
        # return string
    return temp

def sentString(cour,arr):
    temp = ""
    insertionSortRev(arr,cour)
    # traverse in the string
    for i in range(len(cour)):
        temp += cour[i]
        # temp+= arr[i].__str__()
        if arr[i] is int:
         temp += ' ( ' + str(arr[i]) + ' )'

        else:
            a="{:.4f}".format(arr[i])
            temp += ' ( ' + str(a) + ' )'


        if i != 4:
            temp += ' --> '
        # return string
    return temp

def calcProb(a,cour,b):
    # a= prob b=, c=sorted courier
    temp=[]
    high=max(b)+60
    for i in range(len(cour)) :
        z= (b[i])/high
        # print(z)
        temp.append((a[i])*(1-z))
    insertionSortRev(temp,cour)

    return temp


cour =['City-link Express',        'Pos Laju',        'GDEX',        'J&T',        'DHL' ]


# t=parent()
# time = t.getJourneyTime()
# timeC = t.courier_name.copy()
time= [77, 49, 67, 98, 50]
timeC=cour.copy()
dis=[74.1, 37.2, 55.6, 95.3, 37.3]
disC=cour.copy()
# dis = t.getDistance().copy()
# disC = t.courier_name.copy()


# sent=p2()
# pos=sent.positive
pos=[69, 105, 299, 48, 57, 64, 167, 17, 46, 30, 163, 43, 87, 219, 97]
pos = [(pos[0]+pos[1]+pos[2]),(pos[3]+pos[4]+pos[5]),(pos[6]+pos[7]+pos[8]),(pos[9]+pos[10]+pos[11]),(pos[12]+pos[13]+pos[14])]
posC= cour.copy()

# neg=sent.negative
neg=[29, 70, 232, 26, 32, 33, 93, 1, 15, 32, 44, 51, 96, 152, 32]
neg=[(neg[0]+neg[1]+neg[2]),(neg[3]+neg[4]+neg[5]),(neg[6]+neg[7]+neg[8]),(neg[9]+neg[10]+neg[11]),(neg[12]+neg[13]+neg[14])]
negC = cour.copy()

sentProb=[(pos[0]/(pos[0]+neg[0])),(pos[1]/(pos[1]+neg[1])),(pos[2]/(pos[2]+neg[2])),(pos[3]/(pos[3]+neg[3])),(pos[4]/(pos[4]+neg[4]))]
courProb=cour.copy()

finCou=['City-link Express','Pos Laju','GDEX','J&T','DHL' ]
finProb = calcProb(sentProb,finCou,time)

# toString methods
sTime=timeString(timeC,time)
sDis=disString(disC,dis)
sPos= sentString(posC,pos)
sNeg= sentString(negC,neg)
sSent=sentString(courProb,sentProb)
sFin=sentString(finCou,finProb)

# print(pos)
# print(neg)
print('The Fastest Courier =',sTime)
print('The Shortest Route',sDis)
print('The courier with positive review: ',sPos)
print('The courier with negative review: ',sNeg)
print(sSent)
print(sFin)
