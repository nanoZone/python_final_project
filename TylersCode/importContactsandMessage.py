
def getPreviousLocation(file):
    locationList = []
    with open(file, 'rt') as myfile:    # Open file lorem.txt for reading text
        for line in myfile:             # For each line, read it to a string
            if "LOCATION: " in line:
                locationList.append(line.replace("LOCATION:", ''))
                # print(line.replace("LOCATION:", ''))
return locationList

