'''
CS 3030
Emergency Distress Program
Tyler Bramlett

This file will visually present a person's location and display multple destinations on Google Maps.
On Google Maps, if there is more than one location, it will show the distance/time between them.
It will also pull in data from a EmergencyLog file, and search for LOCATIONs and plot a previous and current location within Google Maps.
'''

import webbrowser
import time
import datetime

# NOTE I WISH TO MAKE THESE DECORATORS TO COMBINE AND MAKE CODE MORE COMPLEX
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


# Global vars across files:
currentStatus = "Safe, Battery Low, Uninjured"

# Call function(s):

createLocationMap(getPreviousLocation("EmergencyLog.txt"))
