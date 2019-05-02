'''
CS 3030
Emergency Distress Program
Tyler Bramlett
This file will log, and save emergency data to a .txt file.
It will pull data to read the contents of the emergency log file directly.
It will also add/stamp time for file thus ensuring location/status update info.
'''

import os
import time
import datetime

def getPreviousLocation(file):
    locationList = []
    with open(file, 'rt') as myfile:    # Open file lorem.txt for reading text
        for line in myfile:             # For each line, read it to a string
            if "LOCATION: " in line:
                locationList.append(line.replace("LOCATION:", ''))
                # print(line.replace("LOCATION:", ''))
return locationList


def readFromFile(file):
    os.getcwd()
    logFile = open(file)
    print(f"\n\nREADING CONTENTS OF FILE: {file}\n\n" + logFile.read())
    time.sleep(1)
    print(logFile.read())
logFile.close()

def readFromFile(fileName):
    os.getcwd()
    logFile = open(fileName, 'r')
    # READLINES() IS A LIST OF STRINGS FOR EACH LINE
return logFile.readlines()
