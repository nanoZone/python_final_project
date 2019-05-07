'''
CS 3030
Emergency Distress Program
Tyler Bramlett
This file will retrieve data from the EmergencyInfo.txt file.
It will save data to variables to be utilized with sending SMS/Emails.
'''

import os
import re


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
