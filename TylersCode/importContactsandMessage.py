'''
CS 3030
Emergency Distress Program
Tyler Bramlett
This file will retrieve data from the EmergencyInfo.txt file.
It will save data to variables to be utilized with sending SMS/Emails.
'''

import os
import time
import re
import datetime


def getLastLocation(file):
    locationList = []
    with open(file, 'rt') as myfile:    # Open file lorem.txt for reading text
        for line in myfile:             # For each line, read it to a string
            if "LOCATION: " in line:
                locationList.append(line.replace("LOCATION:", ''))
                # print(line.replace("LOCATION:", ''))
    return locationList


def readFromFile(fileName):
    os.getcwd()
    logFile = open(fileName, 'r')
    # READLINES() IS A LIST OF STRINGS FOR EACH LINE
    return logFile.readlines()


def findContactInfoInFile(file):
    os.getcwd()
    logFile = open(file)
    print(f"\n\nREADING CONTENTS OF FILE: {file}\n\n" + logFile.read())
    time.sleep(1)
    emailList = re.findall('\S+@\S+', logFile.read())
    phoneList = re.findall('\S[0-9]+\S+-\S[0-9]+', logFile.read())

    # Printing of List
    print("Email addresses within this file are: ", emailList)
    print("Phone numbers within this file are: ", phoneList)

    logFile.close()
