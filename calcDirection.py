import gmaps
import gmplot
import googlemaps
from datetime import datetime

import requests
import distance

class parent:

    courier_name = [
        'City-link Express',
        'Pos Laju',
        'GDEX',
        'J&T',
        'DHL'
    ]

    hub_name = [
        'Port Klang',
        'Petaling Jaya',
        'Batu Caves',
        'Kajang',
        'Sungai Buloh'
    ]

    hub_coordinate_x = [  3.0319924887507144,3.112924170027219,3.265154613796736,2.9441205329488325,3.2127230893650065 ]
    hub_coordinate_y = [ 101.37344116244806,101.63982650389863,101.68024844550233,101.7901521759029,101.57467295692778 ]
    hub_Coor=[]

    distance = []
    journey_time = []
    num=0



    apikey = 'AIzaSyDvwt7Hd1CAesuilqcnLB078V5Qy7UwYeY'  # (your API key here)
    gmap = gmplot.GoogleMapPlotter(3.112924170027219, 101.63982650389863, 14, apikey=apikey)
    gmaps = googlemaps.Client(key='AIzaSyDvwt7Hd1CAesuilqcnLB078V5Qy7UwYeY')
    origin = []
    des = []

    def clearArr(self):
        distance = []
        journey_time = []
        origin = []
        des = []

    def __init__(self):
        print('initiate')

    def setOrigin(self,ori):
        self.origin= self.getGeoCoord(ori)

    def setDest(self,des):
        self.des= self.getGeoCoord(des)
        # self.plotMap();
        self.routeInfo()

    def getGeoCoord(self,address):
        params = {
            'key': self.apikey,
            'address': address.replace(' ', '+')
        }

        base_url = 'https://maps.googleapis.com/maps/api/geocode/json?'

        response = requests.get(base_url, params=params)
        data = response.json()

        if data['status'] == 'OK':
            result = data['results'][0]
            location = result['geometry']['location']
            return location['lat'], location['lng']
        else:
            return

    def setCustNo(self,a):
        self.num=a

    def plotMap(self):
        for i in range(len(self.hub_name)):
            self.gmap.text(self.hub_coordinate_x[i], self.hub_coordinate_y[i], self.hub_name[i])
            # gmap.marker(hub_coordinate_x[i], hub_coordinate_y[i], color='cornflowerblue')

        self.gmap.scatter(self.hub_coordinate_x, self.hub_coordinate_y, 'red', size=400, marker=True)
        way=[(self.hub_coordinate_x[self.short], self.hub_coordinate_y[self.short])]
        self.gmap.directions(origin=self.origin, destination=self.des, waypoints=(way))
        self.dir='cus'+str(self.num)+'.html'
        self.gmap.draw(self.dir)
        print("Success")

    def setHub(self,hub):
        if hub=='City-link Express':
            self.hub_Coor=[(self.hub_coordinate_x[0],self.hub_coordinate_y[0])]

        elif hub==  'Post Laju':
            self.hub_Coor=[(self.hub_coordinate_x[1],self.hub_coordinate_y[1])]

        elif hub=='GDEX':
            self.hub_Coor=[(self.hub_coordinate_x[2],self.hub_coordinate_y[2])]

        elif hub==  'J&T':
            self.hub_Coor=[(self.hub_coordinate_x[3],self.hub_coordinate_y[3])]

        elif hub=='DHL':
            self.hub_Coor=[(self.hub_coordinate_x[4],self.hub_coordinate_y[4])]

    def printCoor(self):
        print(self.distance)
        print(self.journey_time)

    def getJourneyTime(self):
        return self.journey_time

    def getDirectory(self):
        return self.dir

    def getDistance(self):
        return self.distance

    def getShort(self):
        return self.short

    def shortestR(self):
        dup=False
        fastT=self.journey_time[0]
        fastI=0

        for i in range (1,5,1):
            j=self.journey_time[i]
            if j < fastT:
                fastT=j
                fastI=i

            elif j==fastT:
                a=self.distance[fastI]
                b=self.distance[i]
                if b<a:
                    fastT=j
                    fastI=i


        self.short=fastI
        print('Shortest Hub is : '+self.courier_name[fastI])
        print('The time taken is: '+fastT)
        self.plotMap()






    def routeInfo(self):
        # st = ' '.join([str(elem) for elem in self.hub_Coor])
        # print(st)

        self.hub_Coor=[(3.0319924887507144,101.37344116244806),(3.112924170027219,101.63982650389863),(3.265154613796736,101.68024844550233),(2.9441205329488325,101.7901521759029),(3.2127230893650065,101.57467295692778)]
        for i in range (5):
            directions = self.gmaps.directions(origin=self.origin, waypoints=self.hub_Coor[i], destination=self.des,
                                      mode='driving', optimize_waypoints=True)
            self.distance.append(directions[0]['legs'][0]['distance']['text'])
            self.journey_time.append(directions[0]['legs'][0]['duration']['text'])

        self.shortestR()


    # print(self.distance)
    # print(self.journey_time)







