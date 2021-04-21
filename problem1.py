import gmplot

class MapGenerate:
    # Initialise hubs
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
    hub_coordinate_x = [
        3.0319924887507144,
        3.112924170027219,
        3.265154613796736,
        2.9441205329488325,
        3.2127230893650065
    ]
    hub_coordinate_y = [
        101.37344116244806,
        101.63982650389863,
        101.68024844550233,
        101.7901521759029,
        101.57467295692778
    ]

    customer_origin = []
    customer_destination = []
    shortest_path = []
    shortest_name = []
    shortest_index = []

    # Create the map plotter:
    apikey = ''  # (your API key here)
    gmap = gmplot.GoogleMapPlotter(3.112924170027219, 101.63982650389863, 14, apikey=apikey)

    def __init__(self):
        # Mark hub locations
        for i in range(len(self.hub_name)):
            self.gmap.text(self.hub_coordinate_x[i], self.hub_coordinate_y[i], self.hub_name[i])
            # gmap.marker(hub_coordinate_x[i], hub_coordinate_y[i], color='cornflowerblue')

        self.gmap.scatter(self.hub_coordinate_x, self.hub_coordinate_y, 'red', size=400, marker=True)


    def save_Customer(self, number):
        # n = int(input('Enter the number of customers:'))
        for i in range(number):
            print('Customer ', i + 1)
            self.customer_origin.append(input('Origin : '))
            self.customer_destination.append(input('Destination : '))


    def get_Shortest_Path(self):
        map = distance_mapping.MapDistance()
        print('------Suggest least distance for parcel to travel------')
        # Calculate the least distance for parcel to travel for each customer
        for i in range(len(self.customer_origin)):
            shortest = 999999999999
            shortestName = ''
            # index
            print('\n-----------Customer ', i+1, '-----------')
            print('Calculating', end="")

            # Calculate the closest hub for based on origin and destination
            for j in range(len(self.hub_name)):
                print('.', end="")
                total_dist = map.calc_total_distance(self.customer_origin[i], self.customer_destination[i], self.hub_name[j])
                # print('Hub name: ', self.hub_name[j])
                # print('Total distance: ', total_dist)
                if total_dist < shortest:
                    shortest = total_dist
                    index = j
                    shortestName = self.hub_name[j]
                # print('Shortest path: ', shortest)
            self.shortest_name.append(shortestName)
            self.shortest_path.append(shortest)
            self.shortest_index.append(index)

            # self.shortest_path[i]= total_dist
            # Print the details
            print('\n-----------Print shortest path-----------')
            print(self.customer_origin[i], ' ---> ', self.shortest_name[i], ' ---> ', self.customer_destination[i])
            print('Shortest hub name: ', self.shortest_name[i])
            # print('Shortest hub name: ', self.hub_name[self.shortest_index[i]])
            print('Recommended courier company: ', self.courier_name[self.shortest_index[i]])
            print('Shortest distance: ', self.shortest_path[i])


    def draw_HTML(self):
        # Create the final map in HTML
        self.gmap.draw('map.html')

# End class

# Main Class
# Draw line and calculate distance of start and end point crossing the hubs
import distance_mapping


mapGen = MapGenerate()


mapGen.save_Customer(int(input('Enter the number of customers:')))
mapGen.get_Shortest_Path()
mapGen.draw_HTML()





