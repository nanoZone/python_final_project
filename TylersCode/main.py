'''
Python Final Group Project
CS 3030
@group members: Tyler Bramlett, Lucas Garcia, Nate Ross

This is a Emergency Distress program!
This program will log/track/send/update data on a person in a disaster or emergency.
This program will provide an interface and visually show a missing person's location history.
This program utilizes two outside files: EmergencyLog.txt, EmergencyInfo.txt
These files will store data on a person's personal and medical information.
Within the program, the two files will be converted into .pdf so they can be shared to emergency contacts
Emergency contacts will also receive updates on a person's status, condition, and location.
'''

import smtplib
import requests
import re
import webbrowser
import time
import datetime
import os
from fpdf import FPDF
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def sleepDecorator(func):
    def wrapper():
        time.sleep(2)
        func()

    return wrapper


def sendEmail(signal, emailList):
    # list of email_id to send the mail
    email = "EmergencyDistressSignal223@gmail.com"
    password = str(input("\nENTER SERVER PASSWORD >> "))
    send_to_email = 'EmergencyDistressSignal223@gmail.com'
    subject = "+++ EMERGENCY SIGNAL +++"
    message = signal

    msg = MIMEMultipart()
    msg['From'] = email
    msg['To'] = send_to_email
    msg['Subject'] = subject

    # Attach the message to the MIMEMultipart object
    msg.attach(MIMEText(message, 'plain'))

    for i in range(len(emailList)):
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(email, password)
        text = msg.as_string()
        server.sendmail(email, emailList[i], text)
    server.quit()


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
    pdf.output("Emergency_Data.pdf")


@sleepDecorator
def findWeatherData():
    # api key
    api_key = "9d0dd491847df6d883ef71401d8af3ec"
    # base url variable to store url
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    # enter city name
    city_name = input("\nENTER THE CURRENT CITY YOU ARE LOCATED IN >> ")
    # complete_url variable to store complete url address
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name
    # return respone object and get method
    response = requests.get(complete_url)
    # json method of response object to convert json format data to python
    x = response.json()

    print("\nPrinting Weather Data: " + str(x))
    # check the value of "cod" key is equal to "404", means city is
    # found, otherwise city is not found
    time.sleep(2)
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
    print("\n\nCURRENT CONDITION: " + str(status))
    print("CURRENT LOCATION: " + str(address))
    print("PIN-POINTING POSITION ON GOOGLE MAPS ...\n")
    webbrowser.open("https://www.google.com/maps/search/" + str(address))
    return address


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
    with open(file, 'rt') as myfile:  # Open file lorem.txt for reading text
        for line in myfile:  # For each line, read it to a string
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


def findContactInfoInFile(file):
    os.getcwd()
    logFile = open(file)
    string = logFile.read()
    emailList = re.findall('\S+@\S+', string)
    phoneNumRegex = re.compile(r"\d\d\d-\d\d\d-\d\d\d\d")
    phoneList = phoneNumRegex.findall(string)

    # Printing of List
    print(f"Email addresses within {file} are: ", emailList)
    print(f"Phone numbers within {file} are: ", phoneList)
    logFile.close()
    return emailList


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


def enterContactInfo(targetFile):
    infoFile = open(targetFile, "w")

    # Personal
    idNum = str(input("\nENTER A 5 DIGIT ID NUMBER:"))
    infoFile.write("ID Number: " + idNum + "\n")
    personName = str(input("\nENTER A FIRST AND LAST NAME:"))
    infoFile.write("Full Name: " + personName + "\n")
    dateofbirth = str(input("\nENTER A DATE OF BIRTH IN THE FORMAT MM-DD-YYYY:"))
    infoFile.write("Date Of Birth: " + dateofbirth + "\n")

    # Medical
    medCondition = str(input("\nENTER A MEDICAL CONDITION(S) OR ENTER N/A:"))
    infoFile.write("Medical Condition(s): " + medCondition + "\n")
    allergies = str(input("\nENTER ALLERGIES OR ENTER N/A:"))
    infoFile.write("Allergy(s): " + allergies + "\n")
    medications = str(input("\nENTER ANY MEDICATIONS OR ENTER N/A:"))
    infoFile.write("Medications: " + medications + "\n")
    bloodType = str(input("\nENTER A BLOODTYPE OR ENTER 'UNKNOWN':"))
    infoFile.write("BloodType: " + bloodType + "\n")

    # Contacts:
    print("\nHOW MANY EMERGENCY CONTACTS DO YOU WISH TO ENTER?")
    contactAmount = int(input())

    for i in range(0, contactAmount):
        # Contact Loop
        num = i + 1
        contactName = str(input("\nENTER AN EMERGENCY CONTACT (FULL NAME) :"))
        infoFile.write("Contact " + str(num) + " Name: " + str(contactName) + "\n")
        contactNum = str(input("\nENTER THEIR PHONE NUMBER IN THE FORMAT 000-000-0000 :"))
        infoFile.write("Contact " + str(num) + " Number: " + str(contactNum) + "\n")
        contactEmail = str(input("\nENTER THEIR EMAIL IN THE FORMAT xxxxx@mail.com :"))
        infoFile.write("Contact " + str(num) + " Email: " + str(contactEmail) + "\n")

    infoFile.close()


# SMALLER BASIC FUNCTIONS
def checkPosition():
    print("\nREPORT YOUR CURRENT POSITION/ADDRESS:\n")
    address = str(input())
    return address


def checkCondition():
    print("\nREPORT YOUR CURRENT CONDITION/HEALTH:\n")
    status = str(input())
    return status


def displayCurrentTime():
    ts = time.gmtime()
    print("\nTIME STAMPED:")
    print(time.strftime("%x %X", ts))
    # 03/05/19 20:40:40


def addToFile(data, file):
    os.getcwd()
    logFile = open(file, "a")
    logFile.write(data + "\n")
    logFile.write(str(datetime.datetime.now()) + "\n")
    logFile.close()


# MAIN SERVER:


# LAMBDA FUNCTIONS / DECORATORS / COMMENTS !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# File names to use:
emergencyLogFile = "EmergencyLog.txt"
emergencyInfoFile = "EmergencyInfo.txt"

print("\n\n\n+++ EMERGENCY DISTRESS PROGRAM +++")
print("\n")

# Ask for data to enter or use a file to use instead
c = 'N'
print("\nWOULD YOU LIKE TO ENTER IN NEW PERSONAL/MEDICAL INFO [Y] OR USE ALREADY EXISTING DATA [N] ?")
c = input().upper()

if c == 'Y':
    enterContactInfo(emergencyInfoFile)

# Converts the Emergency Medical/Personal Data to a sharable .pdf
exportAsPDF(readLinesFromFile(emergencyInfoFile))

# Show info file contents
readContentsFromFile(emergencyInfoFile)

# Look for contacts within data file
print(f"\nFINDING CONTACT INFORMATION WITHIN {emergencyInfoFile} TO SEND UPDATE(s) ...")
emails = findContactInfoInFile(emergencyInfoFile)

# Start with a base location and status:
currentPosition = checkPosition()
currentStatus = checkCondition()

# Upload this data to the log:
addToFile("\nLOCATION: " + currentPosition, emergencyLogFile)
addToFile("STATUS: " + currentStatus, emergencyLogFile)

# Show location:
reportLocation(currentPosition, currentStatus)

# Ask for location updates
while True:
    strIn = input("\nUPDATE LOCATION AND STATUS CONDITIONS(s)? Enter [YES] or [NO] >> ")
    strIn = strIn.upper()
    if strIn == "NO" or strIn != "YES":
        if strIn != "NO":
            print("\nYOU HAVE NOT ENTERED A CORRECT STRING!!!")
            break
        break
    # Enter a  new location and status:
    currentPosition = checkPosition()
    currentStatus = checkCondition()

    # Upload this data to the log, again:
    addToFile("\nLOCATION: " + currentPosition, emergencyLogFile)
    addToFile("STATUS: " + currentStatus, emergencyLogFile)
    # Pin point onto google maps
    reportLocation(currentPosition, currentStatus)

# Track previous locations onto Google Maps
createLocationMap(getPreviousLocation(emergencyLogFile))

# Send data to them (SMS/Email)
content = str(
    "\nCURRENT LOCATION: " + currentPosition + "\nCURRENT CONDITION/STATUS: " + currentStatus)
sendEmail(content, emails)

# Web scrape for local weather info
findWeatherData()

# Save logging to .pdf
print("\nSAVING LOG DATA TO .pdf")
exportAsPDF(readLinesFromFile(emergencyLogFile))

# Show log file contents
time.sleep(3)
print(f"\nCONTENTS OF {emergencyLogFile} : \n")
readContentsFromFile(emergencyLogFile)

# Share logging file
