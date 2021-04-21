import geopy
import ipywidgets as ipywidgets
from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter
from geopy import distance


# Reference
# https://github.com/groundhogday321/python-geocoding-distance-measurement-with-geopy/blob/master/Python%20Geocoding%20%26%20Distance%20Measurement%20with%20GeoPy.ipynb
# https://www.youtube.com/watch?v=3jj_5kVmPLs
# import gmplot
# apikey = '' # (your API key here)
# gmap = gmplot.GoogleMapPlotter(3.519863, 101.538116, 14, apikey=apikey)
#
# gmap.directions(
#     (3.0319924887507144, 101.37344116244806),
#     (3.1000170516638885, 101.53071480907951),
#     waypoints=[
#         (3.0319924887507144, 101.37344116244806),
#         (3.3615395462207878, 101.56318183511695),
#         (3.1000170516638885, 101.53071480907951)
#     ]
# )
#
# gmap.text(3.0319924887507144, 101.37344116244806, 'Port Klang')
#
#
# ############################################
#
# # Mark hob location
# gmap.marker(3.0319924887507144, 101.37344116244806 , color='cornflowerblue')
#
# gmap.marker(3.3615395462207878, 101.56318183511695 , color='cornflowerblue')
# gmap.marker(3.1000170516638885, 101.53071480907951 , color='cornflowerblue')
#
# # Outline the Distance:
# distance = zip(*[
#     (3.0319924887507144, 101.37344116244806 ),
#     (3.3615395462207878, 101.56318183511695),
#     (3.1000170516638885, 101.53071480907951)
# ])
#
# gmap.polygon(*distance, color='cornflowerblue', edge_width=10)
#
# gmap.draw('map.html')


class MapDistance:

    # Calculate the distance of 2 points and return a double
    def calculate_distance(self, origin, dest):
        # print('Calculating distance ...')
        # for i in range(len(origin)):
        pointA = Nominatim(user_agent='tutorial').geocode(origin)
        pointB = Nominatim(user_agent='tutorial').geocode(dest)
        # print('Customer ', i+1, ' :')
        # print(origin, ' ---> ', dest)
        hold_dist = round(distance.distance((pointA.latitude, pointA.longitude), (pointB.latitude, pointB.longitude)).kilometers, 2)
        # print(hold_dist, 'km')
        return hold_dist

    # Returns coordinates and other details of a location based on 'name'
    def get_Location(self, location):
        return Nominatim(user_agent='tutorial').geocode(location)

    def calc_total_distance(self, start, end, hub_location):
        map = MapDistance()
        # print('Calculating distance ...')
        pointA = Nominatim(user_agent='tutorial').geocode(start)
        pointB = Nominatim(user_agent='tutorial').geocode(end)
        pointC = Nominatim(user_agent='tutorial').geocode(hub_location)
        # print(start, ' ---> ', hub_location, ' ---> ', end)
        # hold_dist_1 = round(distance.distance((pointA.latitude, pointA.longitude), (pointB.latitude, pointB.longitude)).kilometers, 2)
        # hold_dist_2 = round(distance.distance((pointA.latitude, pointA.longitude), (pointB.latitude, pointB.longitude)).kilometers, 2)
        total_dist = map.calculate_distance(start, hub_location) + map.calculate_distance(hub_location, end)
        # print(total_dist, 'km')
        return round(total_dist, 2)


# Main Methods

# map = MapDistance()
# n = int(input('Enter the number of customers:'))
# customer_origin = []
# customer_destination = []

# for i in range(n):
#     print('Customer ',i+1)
#     customer_origin.append(input('Origin : '))
#     customer_destination.append(input('Destination : '))
# map.calculate_distance(customer_origin, customer_destination)


# print(customer_origin)
# print(customer_destination)



# indy_500_address = 'Rawang'
# indy_500 = Nominatim(user_agent='tutorial').geocode(indy_500_address)
#
# print(indy_500.latitude, indy_500.longitude)
# print(distance.distance((31.953765, -89.234505), (30.685861, -95.017928)).kilometers)
# indy_500.raw





