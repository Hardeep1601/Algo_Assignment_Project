import gmplot
import googlemaps

import requests


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

    def __init__(self):
        self.distance = []
        self.journey_time = []
        self.num = 0
        self.gmap = gmplot.GoogleMapPlotter(3.112924170027219, 101.639826504389863, 14, apikey=self.apikey)
        self.gmaps = googlemaps.Client(key='AIzaSyDvwt7Hd1CAesuilqcnLB078V5Qy7UwYeY')
        print('initiate')

    def setOrigin(self,ori):
        self.ori = ori
        self.origin= self.getGeoCoord(ori)

    def setDest(self,des):
        self.dest = des
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
        gmap = gmplot.GoogleMapPlotter(3.112924170027219, 101.63982650389863, 14, apikey=self.apikey)
        for i in range(len(self.hub_name)):
            gmap.text(self.hub_coordinate_x[i], self.hub_coordinate_y[i], self.courier_name[i])
            gmap.marker(self.hub_coordinate_x[i], self.hub_coordinate_y[i], color='pink')

        self.gmap.scatter(self.hub_coordinate_x, self.hub_coordinate_y, 'red', size=400, marker=True)
        way = [(self.hub_coordinate_x[self.short], self.hub_coordinate_y[self.short])]
        gmap.directions(origin=self.origin, destination=self.des, waypoints=(way))

        dir = 'cus' + str(self.num) + '.html'
        gmap.draw(dir)
        self.allMap()

    def allMap(self):
        for i in range(len(self.hub_name)):
            way = [(self.hub_coordinate_x[i], self.hub_coordinate_y[i])]
            self.gmap.directions(origin=self.origin, destination=self.des, waypoints=(way))
            self.dir = 'cus' + str(self.num) + 'all' + '.html'
            self.gmap.draw(self.dir)

        print("Success")

    def setHub(self, hub):
        if hub == 'City-link Express':
            self.hub_Coor = [(self.hub_coordinate_x[0], self.hub_coordinate_y[0])]

        elif hub == 'Post Laju':
            self.hub_Coor = [(self.hub_coordinate_x[1], self.hub_coordinate_y[1])]

        elif hub == 'GDEX':
            self.hub_Coor = [(self.hub_coordinate_x[2], self.hub_coordinate_y[2])]

        elif hub == 'J&T':
            self.hub_Coor = [(self.hub_coordinate_x[3], self.hub_coordinate_y[3])]

        elif hub == 'DHL':
            self.hub_Coor = [(self.hub_coordinate_x[4], self.hub_coordinate_y[4])]

        gmap = gmplot.GoogleMapPlotter(3.112924170027219, 101.63982650389863, 14, apikey=self.apikey)
        for i in range(len(self.hub_name)):
            gmap.text(self.hub_coordinate_x[i], self.hub_coordinate_y[i], self.courier_name[i])
            gmap.marker(self.hub_coordinate_x[i], self.hub_coordinate_y[i], color='pink')

        gmap.directions(origin=self.origin, destination=self.des, waypoints=(self.hub_Coor))
        dir = 'cus' + str(self.num) + '.html'
        gmap.draw(dir)

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
        dup = False
        fastT = self.journey_time[0]
        fastI = 0

        for i in range(1, 5, 1):
            j = self.journey_time[i]
            # print(type(j))
            if j < fastT:
                fastT = j
                fastI = i

            elif j == fastT:
                a = self.distance[fastI]
                b = self.distance[i]

                if b < a:
                    fastT = j
                    fastI = i

        self.short = fastI
        print('Shortest Hub is : ' + self.courier_name[fastI])
        print('The time taken is: ' + str(fastT))
        self.plotMap()

    def routeDis(self):
        bass_url = 'https://maps.googleapis.com/maps/api/distancematrix/json?origins='
        origin = self.ori.replace(' ', '+')
        des = self.dest.replace(' ', '+')
        fin_url = bass_url + origin + '&destinations=' + des + '&mode=car&key=' + 'AIzaSyDvwt7Hd1CAesuilqcnLB078V5Qy7UwYeY'
        response = requests.get(fin_url).json()
        return (response['rows'][0]['elements'][0]['distance']['text'], response['rows'][0]['elements'][0]['duration']['text'])

    def routeInfo(self):

        self.hub_Coor = [(3.0319924887507144, 101.37344116244806), (3.112924170027219, 101.63982650389863),
                         (3.265154613796736, 101.68024844550233), (2.9441205329488325, 101.7901521759029),
                         (3.2127230893650065, 101.57467295692778)]
        for i in range(5):
            directions = self.gmaps.directions(origin=self.origin, destination=self.hub_Coor[i], mode='driving')
            direc = self.gmaps.directions(origin=self.hub_Coor[i], destination=self.des,
                                          mode='driving')

            temp = self.process(directions, direc)
            print(temp)
            self.distance.append(temp[0])
            self.journey_time.append(temp[1])
            # print(self.distance.)

        self.shortestR()

    def process(self, a, b):
        d1 = (a[0]['legs'][0]['distance']['text']).split(' ')
        d2 = (b[0]['legs'][0]['distance']['text']).split(' ')
        dis = round(float(d1[0]) + float(d2[0]), 2)
        t1 = (a[0]['legs'][0]['duration']['text']).split(' ')
        t2 = (b[0]['legs'][0]['duration']['text']).split(' ')
        jT = 0;
        if t1[1] == t2[1]:
            if len(t1) == 2:
                jT = int(t1[0]) + int(t2[0])
            else:
                jT = int(t1[0]) * 60 + int(t2[0] * 60) + int(t1[2]) + int(t2[2])

        else:
            if len(t1) != 2:
                jT = int(t1[0]) * 60 + int(t1[2]) + int(t2[0])
            else:
                jT = int(t1[0]) * 60 + int(t1[0]) + int(t2[2])

        return dis, jT












