# import gmplot package
import gmplot

latitude_list = [30.3358376, 30.307977, 30.3216419]
longitude_list = [77.8701919, 78.048457, 78.0413095]

gmap = gmplot.GoogleMapPlotter(30.3164945,78.03219179999999, 13)

# scatter method of map object
# scatter points on the google map
gmap.scatter(latitude_list, longitude_list, '# FF0000',
              size=40, marker=False)

# Plot method Draw a line in
# between given coordinates
gmap.plot(latitude_list, longitude_list,
           'cornflowerblue', edge_width=2.5)

gmap.draw("C:\\Users\\user\\Desktop\\map13.html")