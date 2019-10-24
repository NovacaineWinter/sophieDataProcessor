import csv
import copy
from configuration import filterPercent, timeCol, nameCol, repCol, filterCol, inputFileName, outputFileName

maxRepNumber = 0  # ignore this - it gets overwritten


def parseData(data):
    global maxRepNumber
    toReturn = []
    incorrectCount = 0
    for line in data:

        try:
            # make sure everything is of the right variable type
            line[repCol] = int(line[repCol])
            line[filterCol] = float(line[filterCol])
            line[timeCol] = int(line[timeCol])
            line[nameCol] = int(line[nameCol])

            # Work out what the maximum repetition number is
            if line[repCol] > maxRepNumber:
                maxRepNumber = line[repCol]
            toReturn.append(line)
        except:
            incorrectCount += 1

    print("")
    if incorrectCount > 0:
        print("Loaded "+str(len(data))+' data points from file '+inputFileName)
        print("Accepted "+str(len(toReturn))+" data points")
        print( "Discarded "+str(incorrectCount)+' rows as they contain incorrect variable types')
        print(" ")
        print('time, name and repetition columns can only contain integers, the column to filter by must be numeric')
        print(" ")
        print(" ")
    else:
        print("Loaded "+str(len(data))+' data points from file '+inputFileName)
        print("Accepted "+str(len(toReturn))+" data points")

    print("------------------------------------------------------------------")
    return toReturn


def getUniqueRiceLines(rices):
    # loop through to get all the names of the rice into one big long list
    allRice = []
    for rice in rices:
        allRice.append(rice[nameCol])

    uniqueRice = list(set(allRice))  # set is a data structure that cannot have duplicates in, turn it into a set then turn it back into a list

    return uniqueRice




# 'r' is read. read as opposed to write, Universal is allowing for maximum compatibility with each csv format
f = open(inputFileName, 'r')

# pass the file to the csv reader
rawdata = csv.reader(f)
allData = []
for row in rawdata:
    allData.append(row)


allData = parseData(allData)

percentile = float(float(int(filterPercent) / 100))

uniqueRice = getUniqueRiceLines(allData)

print('Detected ' + str(len(uniqueRice)) + ' unique data series')
print("------------------------------------------------------------------")

"""
Create the places we are going to store data 
"""

dataStore = {}  # create a place to store the data while we are working on it
maxVals = {}  # here we will store the maximum gs values for each rice in order to work out 95%
dataOutput = {}

dataHolder = []
maxList = []


for a in range(0, maxRepNumber):
    dataHolder.append([])
    maxList.append(0)


for rice in uniqueRice:
    dataStore[rice] = copy.copy(dataHolder)  # create an empty list called by the name of the rice

    dataOutput[rice] = copy.copy(dataHolder)  # create an empty list called by the name of the rice

    maxVals[rice] = copy.copy(maxList)  # create an zero var for storing the max gs values for each


# Put the data points into the dataStore by name and rep number
for i in range(1, len(allData)):
    point = allData[i]
    dataindex = (int(point[repCol]) - 1)  # rep number zero indexed
    dataStore[point[nameCol]][dataindex].append(point)

# figure out the maximum values for each name and rep number
for theRice in uniqueRice:
    for k in range(0, maxRepNumber):
        numDataPoints = len(dataStore[theRice][k])
        for data in dataStore[theRice][k]:

            if float(data[filterCol]) > maxVals[theRice][k]:
                maxVals[theRice][k] = float(data[filterCol])

        dataStore[theRice][k] = sorted(dataStore[theRice][k], key=lambda k: float(k[timeCol]))


# we now have the data segmented up by rice, and we have the maximum filter values for each
# lets go through again and find out which ones are below 95%

appended = 0
toCSV = []


allData = sorted(allData, key=lambda k: float(k[nameCol]))
allData = sorted(allData, key=lambda k: float(k[timeCol]))

for data in allData:
    if data[filterCol] < maxVals[data[nameCol]][(data[repCol]-1)] * percentile:
        toCSV.append(data)
        appended+=1

print(str(len(toCSV)) + ' data points exported to export.csv')
print(str(len(allData) - len(toCSV)) + ' data points were above '+str(filterPercent)+"% of the maximum for its repetition")
print("")
print("")
print("outputting " + str(len(toCSV)) + " data points to csv file "+outputFileName)

with open(outputFileName, 'w') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerows(toCSV)

csvFile.close()
