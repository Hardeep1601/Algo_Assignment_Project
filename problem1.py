import gmplot

# Create the map plotter:
apikey = '' # (your API key here)
gmap = gmplot.GoogleMapPlotter(3.519863, 101.538116, 14, apikey=apikey)

#Initialise hubs
hub_name = [
    'Port Klang',
    'Petaling Jaya',
    'Batu Caves',
    'Kajang',
    'Sungai Buloh'
]
hub_coordinate_x = [
    3.0319924887507144,
    3.112924170027219,
    3.265154613796736,
    2.9441205329488325,
    3.2127230893650065
]
hub_coordinate_y =[
    101.37344116244806,
    101.63982650389863,
    101.68024844550233,
    101.7901521759029,
    101.57467295692778
]

# Mark hub locations
for i in range(len(hub_name)):
    gmap.text(hub_coordinate_x[i], hub_coordinate_y[i], hub_name[i])
    gmap.marker(hub_coordinate_x[i], hub_coordinate_y[i], color='cornflowerblue')





# Outline the Distance between locations:
distance = zip(*[
    (3.0319924887507144, 101.37344116244806 ),
    (3.3615395462207878, 101.56318183511695),
    (3.1000170516638885, 101.53071480907951)
])

gmap.polygon(*distance, color='cornflowerblue', edge_width=10)
# gmap.directions()
print(distance)
gmap.draw('map.html')