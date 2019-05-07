#! Python3
'''
Final Group Project
CS 3020
@author Tyler Bramlett
This is a Emergency Distress program!
'''

import requests
import re
import webbrowser
import time
import datetime
import os
from fpdf import FPDF


# Create decorator for pdf function, to read from file then exported as a .pdf
def readLinesFromFile(fileName):
    os.getcwd()
    logFile = open(fileName, 'r')
    # READLINES() IS A LIST OF STRINGS FOR EACH LINE
    return logFile.readlines()


def exportAsPDF(message):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Courier", size=12)
    for line in message:
        pdf.cell(200, 10, txt=line, ln=1, align="A")
    pdf.output("simple_demo.pdf")


def findWeatherData():
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


def reportLocation(address, status):
    print("\n\nPERSON'S CONDITION: " + str(status))
    print("LAST KNOWN LOCATION: " + str(address))
    print("PIN-POINTING POSITION ON GOOGLE MAPS ...\n")
    webbrowser.open("https://www.google.com/maps/search/" + str(address))


def createLocationMap(locations):
    if len(locations) >= 2:
        print("\n\nPREVIOUSLY KNOWN LOCATION: " + str(locations[-2]))
        print("LAST KNOWN LOCATION: " + str(locations[-1]))
        print("TRACKING PERSONS LOCATIONS ON GOOGLE MAPS ...\n")
        webbrowser.open("https://www.google.com/maps/dir/" + str(locations[-1]) + "/" + str(locations[-2]))
    elif len(locations) >= 1:
        print("LAST KNOWN LOCATION: " + str(locations[-1]))
        print("TRACKING PERSONS LOCATIONS ON GOOGLE MAPS ...\n")
        webbrowser.open("https://www.google.com/maps/dir/" + str(locations[-1]))


def getPreviousLocation(file):
    locationList = []
    with open(file, 'rt') as myfile:    # Open file lorem.txt for reading text
        for line in myfile:             # For each line, read it to a string
            if "LOCATION: " in line:
                locationList.append(line.replace("LOCATION:", ''))
                # print(line.replace("LOCATION:", ''))
    return locationList


def readContentsFromFile(file):
    os.getcwd()
    logFile = open(file)
    print(f"\n\nREADING CONTENTS OF FILE: {file}\n\n" + logFile.read())
    time.sleep(1)
    print(logFile.read())
    logFile.close()


def addToFile(data, file):
    os.getcwd()
    logFile = open(file, "a")
    logFile.write(data + "\n")
    logFile.write(str(datetime.datetime.now()) + "\n")
    logFile.close()


def findContactInfoInFile(file):

    os.getcwd()
    logFile = open(file)
    string = logFile.read()
    emailList = re.findall('\S+@\S+', string)
    phoneNumRegex = re.compile(r"\d\d\d-\d\d\d-\d\d\d\d")
    phoneList = phoneNumRegex.findall(string)

    # Printing of List
    print("Email addresses within this file are: ", emailList)
    print("Phone numbers within this file are: ", phoneList)

    logFile.close()


def regexPhoneNumbers():

    # input statement
    s = input("Please provide best phone number xxx-xxx-xxxx, email.")

    # \S matches any non-whitespace character
    # @ for as in the Email
    # + for Repeats a character one or more times
    lst = re.findall('\S+@\S+', s)
    lst1 = re.findall('\S[0-9]+\S+-\S[0-9]+', s)

    # Printing of List
    print("email address: ", lst)
    print("phone numbers are: ", lst1)


findContactInfoInFile("EmergencyInfo.txt")

createLocationMap(getPreviousLocation("EmergencyLog.txt"))


exportAsPDF(readLinesFromFile("EmergencyLog.txt"))


# Global vars to use across files:
currentAddress = "F.E.M.A. Station Colorado Springs"
currentStatus = "Safe, Battery Low, Uninjured"

# File names to use:
fileName001 = "EmergencyLog.txt"
fileName002 = "EmergencyInfo.txt"

# Add specific data to file:
addToFile("\nLOCATION: " + currentAddress, fileName001)
addToFile("STATUS: " + currentStatus, fileName001)

# Read data from these files
readContentsFromFile(fileName001)
readContentsFromFile(fileName002)
