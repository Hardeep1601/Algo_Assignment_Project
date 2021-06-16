# Courier Choice Selector App


To run the program, run the main.py file. The Courier Choice Selector App will launch.

The aim of our project is to help customers in selecting the best courier service available for them within Selangor. 
Our program functions by suggesting a recommended courier tailored to the customer’s needs.. 

This slide shows the details of courier companies and their hub locations.
In our program we defined the courier company name, delivery hub locationa and their respective coordinate. 

The five courier company that are used are:
- Citylink express located in Port Klang
- Poslaju located in Petaling Jaya
- GDEX located in Batu Caves
- J&T in Kajang  
- DHL in Sungai Buloh

This program considers factors such as:
- the quickest and shortest path available in real time using gmplot, Google Geocoding and Google Distance Matrix API.
- best sentiment of courier based on the articles found on web using Beautiful Soup, plotly and nltk.
- suggests with a recommended courier for customer to choose based on an algorithm considering distance, time and sentiment analysis.
