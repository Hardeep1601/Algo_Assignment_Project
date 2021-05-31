# from calcDirection import parent
# from prob2_1 import p2

class sentiment:
    def insertionSort(self,arr,aby):
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

    def insertionSortRev(self,arr,aby):
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


    def timeString(self,cour,arr):
        # initialize an empty string
        self.insertionSort(arr,cour)
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

    def disString(self,cour,arr):
        # initialize an empty string
        temp = ""
        self.insertionSort(arr,cour)
        # traverse in the string
        for i in range (len(cour)):
            temp += cour[i]
            # temp+= arr[i].__str__()

            temp += ' ( '+str(arr[i])+' KM )'


            if i!= 4:
                temp+= ' --> '
            # return string
        return temp

    # Sentiment
    def sentString(self,cour,arr):
        temp = ""
        self.insertionSortRev(arr,cour)
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

    def calcProb(self,a,cour,b):
        # a=sentimentAnalysisProbability, b=timeArr, c=sorted courier
        temp=[]
        high=sum(b)
        for i in range(len(cour)) :
            z= (b[i])/high
            # print(z)
            temp.append((a[i])*(1-z))
        self.insertionSortRev(temp,cour)

        return temp

# Run 1
#  GDEX ( 0.6785 ) --> J&T ( 0.6501 ) --> Pos Laju ( 0.6500 ) --> DHL ( 0.5900 ) --> City-link Express ( 0.5883 )
# Pos Laju ( 0.4484 ) --> DHL ( 0.4033 ) --> GDEX ( 0.3908 ) --> City-link Express ( 0.3016 ) --> J&T ( 0.2469 )
# Run 2
# GDEX ( 0.6785 ) --> J&T ( 0.6501 ) --> Pos Laju ( 0.6500 ) --> DHL ( 0.5900 ) --> City-link Express ( 0.5883 )
# Pos Laju ( 0.5566 ) --> GDEX ( 0.5452 ) --> DHL ( 0.5035 ) --> J&T ( 0.4633 ) --> City-link Express ( 0.4555 )


# cour =['City-link Express',        'Pos Laju',        'GDEX',        'J&T',        'DHL' ]
#
#
# # t=parent()
# # time = t.getJourneyTime()
# # timeC = t.courier_name.copy()
# time= [77, 49, 67, 98, 50]
# timeC=cour.copy()
# dis=[74.1, 37.2, 55.6, 95.3, 37.3]
# disC=cour.copy()
# # dis = t.getDistance().copy()
# # disC = t.courier_name.copy()
#
#
# # sent=p2()
# # pos=sent.positive
# pos=[69, 105, 299, 48, 57, 64, 167, 17, 46, 30, 163, 43, 87, 219, 97]
# pos = [(pos[0]+pos[1]+pos[2]),(pos[3]+pos[4]+pos[5]),(pos[6]+pos[7]+pos[8]),(pos[9]+pos[10]+pos[11]),(pos[12]+pos[13]+pos[14])]
# posC= cour.copy()
#
# # neg=sent.negative
# neg=[29, 70, 232, 26, 32, 33, 93, 1, 15, 32, 44, 51, 96, 152, 32]
# neg=[(neg[0]+neg[1]+neg[2]),(neg[3]+neg[4]+neg[5]),(neg[6]+neg[7]+neg[8]),(neg[9]+neg[10]+neg[11]),(neg[12]+neg[13]+neg[14])]
# negC = cour.copy()
#
# # Sentiment Probability
# sentProb=[(pos[0]/(pos[0]+neg[0])),(pos[1]/(pos[1]+neg[1])),(pos[2]/(pos[2]+neg[2])),(pos[3]/(pos[3]+neg[3])),(pos[4]/(pos[4]+neg[4]))]
# courProb=cour.copy()
#
# # Final courier and probability
# finCou=['City-link Express','Pos Laju','GDEX','J&T','DHL' ]
# finProb = calcProb(sentProb,finCou,time)
#
# # toString methods
# sTime=timeString(timeC,time)
# sDis=disString(disC,dis)
# sPos= sentString(posC,pos)
# sNeg= sentString(negC,neg)
# sSent=sentString(courProb,sentProb)
# sFin=sentString(finCou,finProb)
#
# # print(pos)
# # print(neg)
# print('The Fastest Courier =',sTime)
# print('The Shortest Route',sDis)
# print('The courier with positive review: ',sPos)
# print('The courier with negative review: ',sNeg)
# print(sSent)
# print(sFin)
