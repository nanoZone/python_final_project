# I referenced https://www.geeksforgeeks.org/python-find-current-weather-of-any-city-using-openweathermap-api/ for this
# code

import requests

# print("Hello welcome boys. This code will perform web scrapping to gather data from the following websites: openweathermap.org ")

# api key
api_key = "9d0dd491847df6d883ef71401d8af3ec"

# base url variable to store url
base_url = "http://api.openweathermap.org/data/2.5/weather?"

# enter city name
city_name = input("Enter city name: ")

# complete_url variable to store complete url address
complete_url = base_url + "appid=" + api_key + "&q=" + city_name

# return respone object and get method
response = requests.get(complete_url)

# json method of response object to convert json format data to python
x = response.json()


print("\nPrinting Weather Data: " + str(x))

# check the value of "cod" key is equal to "404", means city is
# found, otherwise city is not found
if x["cod"] != "404":

    # store value of main key in variable y
    y = x["main"]

    # store the value corresponding to "temp" key of y
    current_temperature = y["temp"]

    # store the value corresponding to the "pressure" key of y
    current_pressure = y["pressure"]

    # store the value corresponding to the "humidity" key of y
    current_humidity = y["humidity"]

    # store the value of "weather" key in variable z
    z = x["weather"]

    # store the value corresponding to "description" key at 0 index of z
    weather_description = z[0]["description"]

    print("\n\nTemperature (in kelvin unit) = " +
          str(current_temperature) +
          "\nAtmospheric pressure (in hPa unit) = " +
          str(current_pressure) +
          "\nHumidity (in percentage) = " +
          str(current_humidity) +
          "\nDescription = " +
          str(weather_description))

else:

    print(" City Not Found ")
