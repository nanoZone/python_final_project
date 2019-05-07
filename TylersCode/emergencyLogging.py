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


def readFromFile(file):
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
readFromFile(fileName001)
readFromFile(fileName002)
