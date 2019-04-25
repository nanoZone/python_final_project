'''
CS 3030
Emergency Distress Program
Tyler Bramlett

This file will open and save information to .pdf
This file will read from a .txt file and read in all the lines and search for LOCATIONs and will save it to .pdf
This file will also export information to a pdf, simply called "simple_demo.pdf"
Still working on OPENING a pdf and utilizing its contents
'''

import os
import PyPDF2
from fpdf import FPDF


# Create decorator for pdf function, to read from file then exported as a .pdf
def readFromFile(fileName):
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


def openPDF():
    print("General Kenobi")


exportAsPDF(readFromFile("EmergencyLog.txt"))

